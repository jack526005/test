import requests
import pandas as pd
from bs4 import BeautifulSoup
url="https://www.whit.edu.cn/index.htm"

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)chrome/102.0.0.0 Safari/537.36'}

response = requests.get(url=url,headers=headers)
response.encoding='utf-8'
result=response.text
soup = BeautifulSoup(result,"lxml")
tags=soup.select("div.tab-content a")
all_news=[]
for i in tags:
    title=i.get_text().strip()
    link=i.get('href')
    news={ '标题':title,'链接':link}
    print(news)
    all_news.append(news)
df = pd.DataFrame(all_news)
df.to_csv('芜湖职业技术大学.csv',index=False,encoding='utf-8-sig')



