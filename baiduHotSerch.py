import requests
import pandas as pd
from bs4 import BeautifulSoup
url="https://top.baidu.com/board?tab=realtime"

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)chrome/102.0.0.0 Safari/537.36'}

response = requests.get(url=url,headers=headers)
response.encoding='utf-8'
result=response.text
soup = BeautifulSoup(result,"lxml")
tags=soup.select(".c-single-text-ellipsis")
clickNum=soup.select(".hot-index_1Bl1a")
all_news=[]
num=[]
for i in tags:
    title=i.get_text().strip().replace('#','')
    all_news.append(title)
for i in clickNum:
    clickNum=i.get_text().strip()
    num.append(clickNum)
data_list={'标题':all_news,"热搜指数":num}
data_df=pd.DataFrame(data_list)
data_df.to_csv("百度热搜榜.csv",index=False,encoding='utf-8-sig')

print(all_news)
print(num)
print(data_list)