from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import requests
import random
import re
import base64
import urllib.parse


class BaiduImageDownloader:
    def __init__(self):
        self.download_dir = "baidu_images"
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)

        # 更真实的浏览器配置
        self.chrome_options = Options()
        self.chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        self.chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.chrome_options.add_experimental_option('useAutomationExtension', False)
        self.chrome_options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=self.chrome_options
        )
        self.wait = WebDriverWait(self.driver, 15)

    def close_popups(self):
        """关闭各种弹窗"""
        close_selectors = [
            '.c-btn-close',
            '.dialog-close',
            '.close',
            'button[aria-label="关闭"]',
            '.popup-close'
        ]

        for selector in close_selectors:
            try:
                close_btn = self.driver.find_element(By.CSS_SELECTOR, selector)
                if close_btn.is_displayed():
                    close_btn.click()
                    time.sleep(1)
                    print("关闭弹窗")
            except:
                continue

    def search_images(self, keyword):
        """搜索图片"""
        print("正在访问百度图片...")
        self.driver.get("https://image.baidu.com/")
        time.sleep(3)

        # 尝试关闭弹窗
        self.close_popups()

        try:
            # 方法1: 通过搜索框搜索
            search_box = self.wait.until(
                EC.presence_of_element_located((By.ID, "kw"))
            )
            search_box.clear()
            search_box.send_keys(keyword)
            search_box.send_keys(Keys.ENTER)
            print("通过搜索框搜索成功")
        except:
            # 方法2: 直接构造URL
            encoded_keyword = urllib.parse.quote(keyword)
            search_url = f"https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCwzLDIsNiw0LDUsNyw4LDEsOQ%3D%3D&word={encoded_keyword}"
            self.driver.get(search_url)
            print("通过直接URL搜索")

        time.sleep(3)
        self.close_popups()

    def extract_image_urls(self):
        """提取图片真实URL"""
        image_urls = []

        # 方法1: 查找包含图片信息的script标签
        scripts = self.driver.find_elements(By.TAG_NAME, "script")
        for script in scripts:
            try:
                script_content = script.get_attribute("innerHTML")
                if "objURL" in script_content or "middleURL" in script_content:
                    # 使用正则表达式提取URL
                    urls = re.findall(r'"objURL":"(.*?)"', script_content)
                    urls.extend(re.findall(r'"middleURL":"(.*?)"', script_content))
                    for url in urls:
                        if url.startswith("http"):
                            # 解码URL中的Unicode字符
                            decoded_url = url.encode('utf-8').decode('unicode_escape')
                            image_urls.append(decoded_url)
            except:
                continue

        # 方法2: 直接查找图片元素
        try:
            img_elements = self.driver.find_elements(By.CSS_SELECTOR, "img.main_img")
            for img in img_elements:
                try:
                    src = img.get_attribute("src")
                    data_src = img.get_attribute("data-src")
                    data_imgurl = img.get_attribute("data-imgurl")

                    for url in [src, data_src, data_imgurl]:
                        if url and url.startswith("http") and not url.endswith(".gif"):
                            image_urls.append(url)
                except:
                    continue
        except:
            pass

        return list(set(image_urls))  # 去重

    def scroll_to_load_more(self, target_count):
        """滚动加载更多图片"""
        print("开始滚动加载图片...")
        collected_urls = set()
        scroll_count = 0
        max_scrolls = 20

        while len(collected_urls) < target_count and scroll_count < max_scrolls:
            # 获取当前可见区域的图片URL
            current_urls = self.extract_image_urls()
            collected_urls.update(current_urls)

            print(f"已收集 {len(collected_urls)} 张图片URL，目标 {target_count}")

            if len(collected_urls) >= target_count:
                break

            # 滚动页面
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            scroll_count += 1
            time.sleep(2)  # 等待加载

            # 偶尔向上滚动一点再向下滚动，模拟真实用户
            if scroll_count % 3 == 0:
                self.driver.execute_script("window.scrollBy(0, -500);")
                time.sleep(1)
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        return list(collected_urls)[:target_count]

    def download_image(self, url, keyword, index):
        """下载单张图片"""
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Referer": "https://image.baidu.com/",
                "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
            }

            response = requests.get(url, headers=headers, timeout=15, stream=True)
            response.raise_for_status()

            # 根据内容类型确定文件扩展名
            content_type = response.headers.get('content-type', '')
            if 'jpeg' in content_type or 'jpg' in content_type:
                ext = 'jpg'
            elif 'png' in content_type:
                ext = 'png'
            elif 'gif' in content_type:
                ext = 'gif'
            elif 'webp' in content_type:
                ext = 'webp'
            else:
                # 检查文件内容
                if response.content[:3] == b'\xff\xd8\xff':
                    ext = 'jpg'
                elif response.content[:8] == b'\x89PNG\r\n\x1a\n':
                    ext = 'png'
                else:
                    ext = 'jpg'  # 默认

            # 安全文件名
            safe_keyword = re.sub(r'[\\/*?:"<>|]', '', keyword)
            filename = f"{safe_keyword}_{index:03d}.{ext}"
            filepath = os.path.join(self.download_dir, filename)

            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(8192):
                    f.write(chunk)

            file_size = os.path.getsize(filepath) / 1024
            print(f"✓ 成功下载 {index}: {filename} ({file_size:.1f}KB)")
            return True

        except Exception as e:
            print(f"✗ 下载失败 {index}: {str(e)}")
            return False

    def run(self, keyword, num_images=20):
        """主运行函数"""
        try:
            print(f"开始搜索关键词: {keyword}")
            self.search_images(keyword)

            print(f"目标下载数量: {num_images}")
            image_urls = self.scroll_to_load_more(num_images)

            if not image_urls:
                print("未找到任何图片URL，请检查：")
                print("1. 网络连接是否正常")
                print("2. 关键词是否有效")
                print("3. 页面是否正常加载")
                return

            print(f"找到 {len(image_urls)} 个图片URL，开始下载...")

            success_count = 0
            for i, url in enumerate(image_urls, 1):
                if self.download_image(url, keyword, i):
                    success_count += 1

                # 随机延迟，避免请求过快
                time.sleep(random.uniform(1, 2))

                # 每下载5张图片显示一次进度
                if i % 5 == 0:
                    print(f"下载进度: {i}/{len(image_urls)}")

            print(f"\n下载完成！")
            print(f"成功下载: {success_count}/{len(image_urls)}")
            print(f"保存路径: {os.path.abspath(self.download_dir)}")

        except Exception as e:
            print(f"程序运行出错: {e}")
        finally:
            input("按Enter键关闭浏览器...")
            self.driver.quit()


if __name__ == "__main__":
    downloader = BaiduImageDownloader()

    try:
        keyword = input("请输入图片关键词（默认: 风景）: ").strip()
        if not keyword:
            keyword = "风景"

        while True:
            try:
                num_input = input("请输入下载数量 (1-30, 默认: 10): ").strip()
                if not num_input:
                    num_images = 10
                    break
                num_images = int(num_input)
                if 1 <= num_images <= 30:
                    break
                print("请输入1-30之间的数字")
            except ValueError:
                print("请输入有效数字")

        downloader.run(keyword, num_images)

    except KeyboardInterrupt:
        print("\n程序被用户中断")
    except Exception as e:

        print(f"程序出错: {e}")
