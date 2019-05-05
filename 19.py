#爬取PEXELS图片
from bs4 import BeautifulSoup
import requests
import json
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

url_path = 'https://www.pexels.com/search/'
word = input('请输入你要下载的图片：')
url_tra = 'http://api.microsofttranslator.com/v2/Http.svc/Translate?appId=AFC76A66CF4F434ED080D245C30CF1E71C22959C&from=&to=en&text={}'.format(word)
english_data = requests.get(url_tra)
content = re.findall('<string xmlns="http://schemas.microsoft.com/2003/10/Serialization/">(.*?)</string>',english_data.text,re.S)[0]
url = url_path + content + '/'
wb_data = requests.get(url,headers=headers)
soup = BeautifulSoup(wb_data.text,'lxml')
imgs = soup.select('article > a > img')
list = []
for img in imgs:
    photo = img.get('src')
    list.append(photo)
#https://images.pexels.com/photos/1067333/pexels-photo-1067333.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500
path = 'photo/'
for item in list:
    data = requests.get(item,headers=headers)
    fp =open(path + item.split('?')[0][-10:],'wb')
    fp.write(data.content)
    fp.close()

