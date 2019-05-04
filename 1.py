import requests
from bs4 import BeautifulSoup
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}
res = requests.get('http://bj.xiaozhu.com/',headers=headers)#网站为小猪短租网北京地区网址
soup=BeautifulSoup(res.text,'lxml')#对返回的结果进行解析
#price=soup.select('#page_list > ul > li:nth-child(9) > div.result_btm_con.lodgeunitname > div:nth-child(1) > span > i')
prices=soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > div:nth-child(1) > span > i')
try:
    #print(res)#pycharm中返回结果为<Response [200]>，说明请求网址成功，若为404,400则请求网址失败。
    #print(res.text)
    #print (soup.prettify())
    #print (soup.find_all('div',"r_colsed")) #查找div标签 class='r_colsed'
    #print (soup.find_all('div',attrs={"class":"r_colsed"}))
    for price in prices:
        #print (price) # 从大到小提取需要的信息
        print (price.get_text()) #获取文字信息
except ConnectionError: #出现错误会执行下面的错误
    print ("拒绝连接！")

