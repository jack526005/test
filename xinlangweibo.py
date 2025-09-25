from selenium import webdriver
import datetime
import time
import pandas as pd
from bs4 import BeautifulSoup

url='https://weibo.com/'
browser=webdriver.Chrome()
browser.maximize_window()

browser.get(url)
time.sleep(30)
url='https://s.weibo.com/top/summary?cate=realtimehot'
browser.get(url)
time.sleep(15)
code=browser.page_source

soup = BeautifulSoup(code,"lxml")
rank=soup.select('td.td-01')
title=soup.select('td.td-02 > a')
searches=soup.select('td.td-02 > span')
ranks=[]
titles=[]
searchs=[]

for i in rank:
    r=i.get_text().strip().replace('#','')
    ranks.append(r)
for i in title:
    t=i.get_text().strip().replace('#','')
    titles.append(t)
for i in searches:
    s=i.get_text().strip().replace('#','')
    searchs.append(s)
searchs=['']+searchs

all_news={'序号':ranks,'标题':titles,'热搜指数':searchs}
print(len(ranks),len(titles),len(searchs))
df=pd.DataFrame(all_news)
today=datetime.date.today()
df.to_csv(f'新浪微博热搜榜-{today}.csv',index=False,encoding='utf-8-sig')
