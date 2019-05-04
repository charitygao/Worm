#爬取北京地区短租房的价格
import re
import requests

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}				#加入请求头

res = requests.get('http://bj.xiaozhu.com/',headers=headers)
prices = re.findall('<span class="result_price">¥<i>(.*?)</i>起/晚</span>',res.text) #正则获取价格

for price in prices:
    print (price)