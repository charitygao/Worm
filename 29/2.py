#post提交表单 豆瓣网登陆
import requests
url = 'https://www.douban.com/'
params = {
    'source':'index_nav',
    'form_email':'xxx',
    'form_password':'xxxx',
}

html = requests.post(url,data=params)
print (html.text)