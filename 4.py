#正则表达式
import re
a = 'xxixxoxxixxpxxooxxpp'
infos = re.findall('xx(.*?)xx',a) #贪心算法 (.*?) 匹配任意字符
print (infos)

b = 'one1two2three3'
infos1 = re.search('\d+',b) #search表达式返回的是正则表达式对象
print (infos1) 
print (infos1.group()) #group方法获取信息

infos2 = re.findall('\d+',b)
print (infos2)

phone = '123-4567-1234'
new_phone = re.sub('\D','',phone)
print (new_phone)

c = '<div>指数</div>'
word = re.findall('<div>(.*?)</div>',c)
print (word)

d = '''<div>指数
</div>'''
word1 = re.findall('<div>(.*?)</div>',d,re.S)
print (word1[0].strip()) #strip()去除换行符