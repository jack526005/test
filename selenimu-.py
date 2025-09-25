# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com/')
# time.sleep(1)
# browser.find_element(By.XPATH, '//*[@id="chat-textarea"]').send_keys('中国')
# browser.find_element(By.XPATH, '//*[@id="chat-submit-button"]').click()
# data=browser.page_source
# print(data)
# browser.quit()
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# # 初始化浏览器
# browser = webdriver.Chrome()
#
# try:
#     # 打开百度首页
#     browser.get('https://www.baidu.com/')
#     # 等待页面加载
#     time.sleep(2)
#
#     # 百度首页搜索框的正确ID是"kw"
#     search_box = browser.find_element(By.ID, "kw")
#     search_box.send_keys('10059')
#
#     # 百度首页搜索按钮的正确ID是"su"
#     search_button = browser.find_element(By.ID, "su")
#     search_button.click()
#
#     # 等待搜索结果加载
#     time.sleep(200)
#
#     # 获取页面源代码
#     data = browser.page_source
#     print(data)
#
# finally:
#     # 关闭浏览器
#     browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get('https://www.bilibili.com/')
time.sleep(1)
browser.find_element(By.CLASS_NAME, 'nav-search-input').send_keys('熊出没')
browser.find_element(By.CLASS_NAME, 'nav-search-btn').click()
time.sleep(5)
data = browser.page_source
print(data)
browser.quit()



