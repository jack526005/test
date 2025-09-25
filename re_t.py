import re


text='123Qwe!_@#你我他\t \n\r'
result1=re.findall('\s',text)
result2=re.findall('\S',text)
print(result1)
print(result2)
print("第二组：")
text2='abcaabb'
result3=re.findall('a.b',text2)
result4=re.findall('a?b',text2)
result5=re.findall('a*b',text2)
result6=re.findall('a.*b',text2)
result7=re.findall('a.*?b',text2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)

