from bs4 import BeautifulSoup
import requests
url="https://my.oschina.net/u/4806939/blog/18692955"

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)chrome/102.0.0.0 Safari/537.36'}

response = requests.get(url=url,headers=headers)


result=response.text

soup=BeautifulSoup(result,'lxml')
tag1=soup.select('span')
print(tag1)


