#api调用 
#必应翻译api
import requests
url = 'http://api.microsofttranslator.com/v2/Http.svc/Translate?appId=AFC76A66CF4F434ED080D245C30CF1E71C22959C&from=&to=en&text=考勤计算'

res = requests.get(url)

print (res.text)