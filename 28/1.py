#异步加载 逆向工程
from bs4 import BeautifulSoup
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Mobile Safari/537.36'
}

urls = ['http://www.pexels.com/search/book/?page={}'.format(str(i)) for i in range(1,3)]
list=[]
for url in urls:
    wb_data= requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    imgs = soup.select(' article > a > img')
    for img in imgs:
        photo = img.get('src')
        list.append(photo)

path = 'book/'
for item in list:
    data = requests.get(item,headers=headers)
    fp = open(path+item.split('?')[0][-10:],'wb')
    fp.write(data.content)
    fp.close()