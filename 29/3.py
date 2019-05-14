#利用cookie 模拟登陆
import requests
url = 'https://www.douban.com/'

headers = {
    'Cookie': 'xxxxxx'
}

html = requests.get(url,headers=headers)
print (html.text)