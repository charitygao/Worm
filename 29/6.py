#爬取新浪微博好友圈信息
import requests
import json

headers ={
    'cookie': 'xxxxxx',
    'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Mobile Safari/537.36'
}

f = open('weibo.txt','a+',encoding='utf-8')
def get_info(url,page):
    html = requests.get(url,headers=headers)
    json_data = json.loads(html.text)
    print (json_data)
    card_groups = json_data[0]['card_group']
    for card_group in card_groups:
        f.write(card_group['mblog']['text'].split(' ')[0]+'\n')
    next_cursor = json_data[0]['next_cursor']
    if page<50:
        next_url = 'https://m.weibo.cn/index/friends?format=cards&next_cursor='+str(next_cursor) + '&page=1'
        page+=1
        get_info(next_url,page)
    else:
        pass
        f.close()

if __name__ == '__main__':
    url = 'https://m.weibo.cn/index/friends?format=cards'
    get_info(url,1)