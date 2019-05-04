#使用Xpath
import requests
from lxml import etree
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}
url = 'http://www.qiushibaike.com/text/'
res = requests.get(url,headers=headers)
selector = etree.HTML(res.text)
id = selector.xpath('//*[@id="qiushi_tag_118732380"]/div[1]/a[2]/h2/text()')
print(id)
