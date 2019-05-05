#调用api 实时翻译
import requests
import re

word = input('请输入中文：')
url = 'http://api.microsofttranslator.com/v2/Http.svc/Translate?appId=AFC76A66CF4F434ED080D245C30CF1E71C22959C&from=&to=en&text='+ word
res = requests.get(url)

print (res.text)
english_data=re.findall('<string xmlns="http://schemas.microsoft.com/2003/10/Serialization/">(.*?)</string>',res.text,re.S)[0]
print (english_data)
