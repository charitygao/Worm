#爬取豆瓣电影top250的数据
import requests
from lxml import etree
import re 
import pymysql
import time

conn = pymysql.connect(host='localhost',user='stud',passwd='123456',db='test',port=3306,charset='utf8')
cursor = conn.cursor()

headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2'
}

def get_movie_url(url):
    html = requests.get(url,headers=headers)
    selector = etree.HTML(html.text)
    movie_hrefs = selector.xpath('//div[@class="hd"]/a/@href')
    for movie_href in movie_hrefs:
        get_movie_info(movie_href)

def get_movie_info(url):
    html = requests.get(url,headers=headers)
    selector = etree.HTML(html.text)
    try:
        name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')[0]
        director = selector.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')[0]
        actors = selector.xpath('//*[@id="info"]/span[3]/span[2]')[0]
        actor = actors.xpath('string(.)')
        style = re.findall('<span property="v:genre">(.*?)</span>',html.text,re.S)[0]
        country = re.findall('<span class="pl">制片国家/地区:</span> (.*?)<br/>',html.text,re.S)
        release_time =re.findall('上映日期:</span>.*?>(.*?)</span>',html.text,re.S)[0]
        time =re.findall('片长:</span>.*?>(.*?)</span>',html.text,re.S)[0]
        score = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')[0]
        cursor.execute(
            "insert into doubanmovie (name,director,actor,style,country,release_time,time,score)values(%s,%s,%s,%s,%s,%s,%s,%s)",(str(name),str(director),str(actor),str(style),str(country),str(release_time),str(time),str(score))
        ) 
    except IndexError:
        pass

if __name__ == '__main__':
    urls =['https://movie.douban.com/top250?start={}'.format(str(i)) for i in range(0,26,25)]
    for url in urls:
        get_movie_url(url)
        time.sleep(2)
    conn.commit()