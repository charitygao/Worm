#综合案例2-----爬取酷狗 TOP 500 的数据
import requests
from bs4 import BeautifulSoup
import time #导入相应的库文件

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}				#加入请求头

def get_info(url):
    wb_data = requests.get(url,headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    ranks = soup.select('span.pc_temp_num')
    titles = soup.select('div.pc_temp_songlist > ul > li > a')
    times = soup.select('span.pc_temp_tips_r > span')
    for rank,title,time in zip(ranks,titles,times):
        data={
            'rank':rank.get_text().strip(),
            'singer':title.get_text().split('-')[0],
            'song':title.get_text().split('-')[1], #通过split获取歌手和歌曲信息
            'time':time.get_text().strip()
        }
        print (data) #获取爬虫信息并按字典打印

if __name__ =='__main__': #程序主入口
    urls=['http://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(str(i)) for i in range(1,24)] #构造多页url
    for url in urls:
        get_info(url) #循环调用get_inso()
    time.sleep(1) #睡眠1秒
