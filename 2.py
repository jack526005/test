s=" i am 21 years old  "

print("首字母大写：",s.title())
print("空格替换为：",s.replace(" ","*"))
print("删除字符串前后的空格：",s.strip(" "))
print("将字符串按空格分隔成列表：",s.split())
print("判断字符串是否全为字母",s.isalpha())
print("判断字符串中单词个数：",len(s.split()))
no_digits = ''.join([c for c in s if not c.isdigit()])
print("删除字符串中所有数字后:", repr(no_digits))


