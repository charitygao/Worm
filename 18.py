#爬取图片 先请求图片链接 然后打开文件写入数据
import requests
from lxml import etree

urls = ['http://jandan.net/ooxx/page-{}'.format(str(i)) for i in range(0,20)]

path = 'img/'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

def get_photo(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    photo_urls = selector.xpath('//p/a[@class="view_img_link"]/@href')
    for photo_url in photo_urls:
        data = requests.get('http:'+photo_url,headers=headers)
        fp = open(path + photo_url[-10:],'wb')
        fp.write(data.content)
        fp.close()

for url in urls:
    get_photo(url)