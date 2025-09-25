# import requests
# url='https://www.baidu.com'
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)chrome/102.0.0.0 Safari/537.36'}
# response = requests.get(url=url,headers=headers)
# response.encoding='utf-8'
# result=response.text
# print(result)

import requests
url="https://my.oschina.net/u/8690838/blog/18692883"

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)chrome/102.0.0.0 Safari/537.36'}
params={'items':'[]','page':'1','perPage':'30','totalItems':'0','totalPages':'0'}
response = requests.get(url=url,headers=headers)


result=response.text

print(result)