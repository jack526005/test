import requests
import pandas as pd

params = {
    "tab":'meishi_new' ,
    "act": "pcFeed",
    "pd": 'pc',
    "num": '20'
}
url = "https://haokan.baidu.com/web/video/feed"  # 替换为你的实际接口地址
headers={
    'Cookie': 'H_WISE_SIDS_BFESS=60449_60839_60853_60617_60884_60875; PSTM=1748617973; BIDUPSID=1318922B9612A6CFCDD5F53B580B1152; BAIDUID=96A2DDF6BD454F939EC1EFDB699ADD34:FG=1; BAIDUID_BFESS=96A2DDF6BD454F939EC1EFDB699ADD34:FG=1; H_PS_PSSID=63144_63325_64313_64646_64699_64816_64865_64873_64835_64905_64930_64978_65019_65123_65189_65204_65227_65249_65255_65275_65325_65376_65417; H_WISE_SIDS=63144_63325_64313_64646_64699_64816_64865_64873_64835_64905_64930_64978_65019_65123_65189_65204_65227_65249_65255_65275_65325_65376_65417; ZFY=kVLS8QUefBPEqVmsyEi2vhDC6SL0GY:Bwq2Lq:A1QuDSM:C; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1758712605; HMACCOUNT=0F2A9AD9BE0ACE94; arialoadData=false; ab_sr=1.0.1_OWEyYzBiY2FmMjg3ODIyMmU0OTg3MzcyMTlmYTlhZTNhZDM2MWFiZGFiODVmMDYwNGY5MjRkZWY0YjkwMDJkNjNlOTU4YTM1YzY5OTcwYTBhZTBmYjMwYzFiMWNiMTlkN2JjMTQ3NjFmYWQ3OGMyNTFmNDg2M2MzZDk1NGJkODdmM2E3YWNiMzcwNDllMDViMDg5MzRhZjZjMmZjZjQ5Nw==; reptileData=%7B%22data%22%3A%22e946729d7955cca09c857049aec85ca1aed067292eb64bdb8dbb856506aec9da31662f9ac341e64e1ead894f8c70c798dfe6f0e66c500cabca7a3d706245fe4a0460fafd64509ad1d0c7b9e69324ebc1d7057a408f39a4924e924c76b75c6fae%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%22aa600cb3%22%7D; hkpcSearch=%u53F0%u98CE%u81F4%u53F0%u6E7E%u53D1%u751F%u6D2A%u707E; ppfuid=FOCoIC3q5fKa8fgJnwzbE67EJ49BGJeplOzf+4l4EOvDuu2RXBRv6R3A1AZMa49I27C0gDDLrJyxcIIeAeEhD8JYsoLTpBiaCXhLqvzbzmvy3SeAW17tKgNq/Xx+RgOdb8TWCFe62MVrDTY6lMf2GrfqL8c87KLF2qFER3obJGl3ixVdpjxtMIx1uoaGiQnXGEimjy3MrXEpSuItnI4KD61Z2nRBM5IUB40fVJd0YGjl3B58tMlzSV2JFI12xxmW2U2yEdmgaoTKG87qC2BxCxJsVwXkGdF24AsEQ3K5XBbh9EHAWDOg2T1ejpq0s2eFy9ar/j566XqWDobGoNNfmfpaEhZpob9le2b5QIEdiQdtJfhN1eLb/i/C9hcVPjDWFCMUN0p4SXVVUMsKNJv2T2Q0Rs14gDuqHJ3rxHJuOGO4LkPV+7TROLMG0V6r0A++zkWOdjFiy1eD/0R8HcRWYvoof6mSAGHJpuboM5joRsCp+HBavJhpxl858h16cMtKQmxzisHOxsE/KMoDNYYE7ucLE22Bi0Ojbor7y6SXfVj7+B4iuZO+f7FUDWABtt/WWQqHKVfXMaw5WUmKnfSR5wwQa+N01amx6X+p+x97kkGmoNOSwxWgGvuezNFuiJQdt51yrWaL9Re9fZveXFsIu/gzGjL50VLcWv2NICayyI8BE9m62pdBPySuv4pVqQ9Sl1uTC//wIcO7QL9nm+0N6JgtCkSAWOZCh7Lr0XP6QztjlyD3bkwYJ4FTiNanaDaD5MA0d2/og8XLWRRrQrrLwt/xHniBzrnzZS0IL2F4LpmpxmYCJZNrnRUkSIDHL7jJSGk66HDxtjKMU4HPNa0dtv9tmNi5OLf3trbXvvpFbLWEB8hf4s5ieWYkugh95AkbJXzxzBwzWy+n7NUONSlz61f6EoK62gY5LGh4PT3C0+8jCe5X+IsGbikc/JdlZKdZHHxUnYx9OEBH0ljzkFSY+Oo6VuGtuVcWQFAbufgkqJnJqWT1fbYVd7Yyx2Kk4cXFJQdKps+jY88nMSivXabqVOFHtiCaV8u3uSe0kPld4zsYRDDc4ujl2xJR5AN3q8OeRvvb9Mxhxs9bjxa5KdKAwMvzbQbq/mwgjd9siXUizBEYRDDc4ujl2xJR5AN3q8Oe1WWULX5oIJzwrbxFaliZTRLbhH0MNlXHePf60sunDcFG4X+UjvIZDl0Se0IQy2dVQs5kL/lku7YbUbPICse0exTllnZC81hhWPgxy+x2ZmXayxvT1iTUpRrGE132K7Dr; RT="z=1&dm=baidu.com&si=b190ad6c-824d-4bc7-bce1-2cb7e591461b&ss=mfxw91rn&sl=4&tt=3qk&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=4ubw&ul=4wln&hd=4x2j"; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1758713128',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)chrome/102.0.0.0 Safari/537.36'}

response = requests.get(url,headers=headers, params=params)
result = response.json()
videos=result['data']['response']['videos']
df=pd.DataFrame(videos)
df=df[['title','previewUrlHttp','fmplaycnt']]
df.columns=['标题','视频链接','播放人数']
df.to_excel('好看视频.xlsx',index=False)
print(df)
print(videos[0])
print(result)
