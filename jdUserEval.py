from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

# 初始化浏览器并访问页面
browser = webdriver.Chrome()
browser.maximize_window()
url = 'https://www.tmall.com/'
browser.get(url)

# 等待页面加载（30秒手动操作时间，可根据需求调整）
time.sleep(30)




# 点击进入评论区

