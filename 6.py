#爬取《斗破苍穹》全文小说
import requests
import re
import time #导入相应库文件

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}				#加入请求头

f = open('doupo.txt','a+') #新建txt文档，追加的方式

def get_info(url): #定义获取信息的函数
    res = requests.get(url,headers=headers)
    if res.status_code == 200: #判断请求码是否是200
        contents = re.findall('<p>(.*?)</p>',res.content.decode('utf-8'),re.S)
        for content in contents:
            f.write(content+'\n') #正则获取数据写入Txt文件
    else:
        pass #不为200就pass掉

if __name__ =='__main__':
    urls = ['http://www.doupoxs.com/doupocangqiong/{}.html'.format(str(i))for i in range(2,1665)] #构造多页url
    for url in urls:
        get_info(url) #循环调用get_info()函数
        time.sleep(1) #睡眠1秒
f.write('你好斗破苍穹！\n')
f.close() #关闭TXT文件