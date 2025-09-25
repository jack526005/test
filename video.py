import os
import time
import random
import requests
import sys
import subprocess
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager


def setup_driver():
    """设置Chrome浏览器驱动（自动管理版本）"""
    chrome_options = Options()
    # 注释掉无头模式以便调试
    chrome_options.add_argument('--headless=new')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1280,720')
    chrome_options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # 随机设置语言，增加伪装性
    languages = ["en-US,en;q=0.9", "zh-CN,zh;q=0.9", "zh-TW,zh;q=0.9"]
    chrome_options.add_argument(f'--lang={random.choice(languages)}')

    try:
        # 自动下载和管理 ChromeDriver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # 进一步隐藏自动化特征
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        })

        return driver
    except Exception as e:
        print(f"启动Chrome浏览器时出错: {e}")
        return None


def search_videos(keyword, num_videos=4):
    """搜索B站视频并获取链接"""
    print(f"开始搜索视频，关键词: {keyword}")

    driver = setup_driver()
    if not driver:
        return []

    try:
        # 编码关键词
        encoded_keyword = quote(keyword)
        url = f"https://search.bilibili.com/all?keyword={encoded_keyword}"

        print("访问B站搜索页面...")
        driver.get(url)

        # 随机等待，避免被识别为爬虫
        time.sleep(random.uniform(3, 5))

        # 模拟更自然的滚动加载
        print("模拟滚动加载内容...")
        scroll_pause_time = random.uniform(1.5, 3)
        last_height = driver.execute_script("return document.body.scrollHeight")

        for i in range(3):
            # 随机位置滚动
            scroll_to = random.randint(int(last_height * 0.6), int(last_height * 0.9))
            driver.execute_script(f"window.scrollTo(0, {scroll_to});")
            time.sleep(scroll_pause_time)

            # 计算新的滚动高度并与上一次比较
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break  # 如果滚动高度相同，说明没有更多内容加载
            last_height = new_height

        # 等待视频元素加载
        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".video-item"))
            )
        except TimeoutException:
            print("页面加载超时，尝试继续...")

        # 优化的选择器策略
        video_links = []

        # 尝试多种选择器，提高兼容性
        selectors = [
            'a[href^="/video/"]',
            '.bili-video-card__wrap > a',
            '.video-item .img-anchor',
            '.search-page .video-item a'
        ]

        for selector in selectors:
            try:
                elements = driver.find_elements(By.CSS_SELECTOR, selector)
                for element in elements:
                    href = element.get_attribute('href')
                    if href and '/video/' in href and href not in video_links:
                        # 确保是完整链接
                        if not href.startswith('http'):
                            href = f"https:{href}" if href.startswith('//') else f"https://www.bilibili.com{href}"
                        video_links.append(href)
                        print(f"找到视频链接: {href}")
                        if len(video_links) >= num_videos:
                            break
                if len(video_links) >= num_videos:
                    break
            except Exception as e:
                print(f"使用选择器 {selector} 时出错: {e}")

        # 如果还没找到足够的视频，尝试XPATH
        if len(video_links) < num_videos:
            try:
                xpath_elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/video/')]")
                for element in xpath_elements:
                    href = element.get_attribute('href')
                    if href and '/video/' in href and href not in video_links:
                        if not href.startswith('http'):
                            href = f"https:{href}" if href.startswith('//') else f"https://www.bilibili.com{href}"
                        video_links.append(href)
                        print(f"找到视频链接: {href}")
                        if len(video_links) >= num_videos:
                            break
            except Exception as e:
                print(f"使用XPATH时出错: {e}")

        return video_links[:num_videos]

    except Exception as e:
        print(f"搜索过程中出错: {e}")
        return []
    finally:
        driver.quit()
        print("浏览器已关闭")


def run_command_with_encoding(cmd, timeout=300):
    """运行命令并处理编码问题"""
    try:
        # 设置UTF-8编码环境
        env = os.environ.copy()
        env['PYTHONIOENCODING'] = 'utf-8'

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            encoding='utf-8',
            errors='replace',  # 替换无法解码的字符
            env=env
        )
        return result
    except subprocess.TimeoutExpired:
        return type('TimeoutResult', (), {'returncode': -1, 'stderr': '命令执行超时'})()
    except Exception as e:
        return type('ErrorResult', (), {'returncode': -1, 'stderr': str(e)})()


def download_videos(video_links, download_path):
    """下载视频"""
    if not video_links:
        print("没有可下载的视频链接")
        return

    print(f"开始下载 {len(video_links)} 个视频...")

    # 检查下载工具是否可用
    tools = ['yt-dlp', 'you-get']
    available_tool = None

    for tool in tools:
        try:
            result = run_command_with_encoding([tool, '--version'])
            if result.returncode == 0:
                available_tool = tool
                print(f"使用下载工具: {tool}")
                break
        except:
            continue

    if not available_tool:
        print("错误: 未找到可用的下载工具 (yt-dlp 或 you-get)")
        print("请安装: pip install yt-dlp")
        return

    # 创建下载日志文件
    log_file = os.path.join(download_path, 'download_log.txt')

    for i, link in enumerate(video_links, 1):
        print(f"\n正在下载第 {i}/{len(video_links)} 个视频: {link}")

        try:
            if available_tool == 'yt-dlp':
                # 优化的下载参数
                cmd = [
                    'yt-dlp',
                    '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                    '--merge-output-format', 'mp4',
                    '--no-warnings',
                    '--console-title',
                    '--restrict-filenames',  # 限制文件名仅包含ASCII字符
                    '-o', f'{download_path}/%(title)s.%(ext)s',
                    link
                ]
            else:  # you-get
                cmd = [
                    'you-get',
                    '--format=mp4',
                    '--output-dir', download_path,
                    '--no-proxy',
                    link
                ]

            print(f"执行命令: {' '.join(cmd)}")

            # 实时输出进度
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding='utf-8',
                errors='replace',
                bufsize=1,
                universal_newlines=True
            )

            # 实时输出进度
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    print(output.strip())

            returncode = process.poll()

            if returncode == 0:
                print(f"✓ 成功下载: {link}")
                with open(log_file, 'a', encoding='utf-8') as f:
                    f.write(f"成功: {link}\n")
            else:
                print(f"✗ 下载失败: {link} (返回码: {returncode})")
                with open(log_file, 'a', encoding='utf-8') as f:
                    f.write(f"失败: {link} (返回码: {returncode})\n")

        except subprocess.TimeoutExpired:
            print(f"✗ 下载超时: {link}")
            with open(log_file, 'a', encoding='utf-8') as f:
                f.write(f"超时: {link}\n")
        except Exception as e:
            print(f"✗ 下载出错: {e}")
            with open(log_file, 'a', encoding='utf-8') as f:
                f.write(f"错误: {link} - {e}\n")

        # 下载间隔，避免请求过于频繁
        time.sleep(random.uniform(2, 5))


def setup_ffmpeg():
    """设置FFmpeg路径"""
    # 尝试多个可能的FFmpeg路径
    possible_paths = [
        r"E:\ffmpeg\ffmpeg-2025-09-22-git-c9168717bf-essentials_build\bin",
        r"E:\ffmpeg-7.1.1-essentials_build\bin",
        r"C:\ffmpeg\bin",
        r"D:\ffmpeg\bin",
        r"C:\Program Files\ffmpeg\bin",
        os.path.join(os.environ.get('PROGRAMFILES', ''), "ffmpeg", "bin")
    ]

    # 检查系统PATH中是否已有ffmpeg
    def is_ffmpeg_available():
        try:
            result = run_command_with_encoding(['ffmpeg', '-version'])
            return result.returncode == 0
        except:
            return False

    if is_ffmpeg_available():
        print("FFmpeg 已在系统PATH中找到")
        return True

    ffmpeg_found = False
    for path in possible_paths:
        if os.path.exists(path) and os.path.isfile(os.path.join(path, 'ffmpeg.exe')):
            os.environ["PATH"] += os.pathsep + path
            print(f"FFmpeg 路径设置成功: {path}")
            ffmpeg_found = True
            break

    if not ffmpeg_found:
        print("警告: 未找到 FFmpeg，可能无法合并视频和音频")
        print("请下载FFmpeg并添加到系统PATH或修改代码中的possible_paths")
    return ffmpeg_found


def main():
    """主函数"""
    # 设置控制台编码为UTF-8
    if sys.platform.startswith('win'):
        try:
            os.system('chcp 65001')  # Windows下设置控制台为UTF-8
        except:
            pass

    # 设置FFmpeg路径
    setup_ffmpeg()

    keyword = input("请输入要搜索的关键字: ").strip()
    if not keyword:
        print("关键字不能为空")
        return

    # 创建下载目录，使用更安全的路径处理
    safe_keyword = "".join([c for c in keyword if c.isalpha() or c.isdigit() or c in '._- ']).rstrip()
    download_path = os.path.join(os.getcwd(), safe_keyword)

    try:
        os.makedirs(download_path, exist_ok=True)
        print(f"下载目录: {download_path}")
    except Exception as e:
        print(f"创建目录失败: {e}")
        return

    # 搜索视频
    video_links = search_videos(keyword)

    if video_links:
        print(f"\n找到 {len(video_links)} 个视频链接:")
        for i, link in enumerate(video_links, 1):
            print(f"{i}. {link}")

        # 下载视频
        download_videos(video_links, download_path)
        print("\n下载任务完成!")
        print(f"详细日志请查看: {os.path.join(download_path, 'download_log.txt')}")
    else:
        print("没有找到相关视频")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"程序运行出错: {e}")
        input("按任意键退出...")
