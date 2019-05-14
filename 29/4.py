#爬取拉钩网招聘信息
import requests
import json
import time
import pymongo

client = pymongo.MongoClient('localhost',27017,username='admin',password='123456')
mydb = client['mydb']
lagou = mydb['lagou']

headers = {
    'Cookie': 'JSESSIONID=ABAAABAAAIAACBI95AE227F9D3FE8EF9AD894A321259550; X_HTTP_TOKEN=42daf4b72327b2817071187551bf5e71415983ed09; _ga=GA1.2.1997497339.1557811708; _gid=GA1.2.1556401461.1557811708; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1557811708; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1557811708; user_trace_token=20190514132827-19f55ee3-7609-11e9-9f4d-5254005c3644; LGSID=20190514132827-19f560f7-7609-11e9-9f4d-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGRID=20190514132827-19f56209-7609-11e9-9f4d-5254005c3644; LGUID=20190514132827-19f56305-7609-11e9-9f4d-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Mobile Safari/537.36'
}

def get_page(url,params):
    html = requests.post(url,data=params,headers=headers)
    json_data = json.loads(html.text)
    print (html.text)
    total_Count = json_data['content']['positionResult']['totalCou nt']
    page_number = int(total_Count/15) if int(total_Count/15)<30 else 30
    get_info(url,page_number)

def get_info(url,page):
    for pn in range(1,page+1):
        params = {
            'first':'true',
            'pn':str(pn),
            'kd':'Python'
        }
        try:
            html = requests.post(url,data=params,headers=headers)
            json_data = json.loads(html.text)
            results = json_data['content']['positionResult']['result']
            for result in results:
                infos = {
                    'businessZones':result['businessZones'],
                    'city':result['city'],
                    'companyFullName':result['companyFullName'],
                    'companyLableList':result['companyLableList'],
                    'companySize':result['companySize'],
                    'district':result['district'],
                    'education':result['education'],
                    'explain':result['explain'],
                    'financeStage':result['financeStage'],
                    'firstType':result['firstType'],
                    'formatCreateTime':result['formatCreateTime'],
                    'gradeDescription':result['gradeDescription'],
                    'imState':result['imState'],
                    'industryField':result['industryField'],
                    'jobNature':result['jobNature'],
                    'positionAdvantage':result['positionAdvantage'],
                    'salary':result['salary'],
                    'secondType':result['secondType'],
                    'workYear':result['workYear']
                }
                lagou.insert_one(infos)
                time.sleep(2)
        except requests.exceptions.ConnectionError:
            pass
if __name__ == '__main__':
    url = 'https://www.lagou.com/jobs/positionAjax.json'
    params = {
        'first':'true',
        'pn':'1',
        'kd':'Python'
    }
    get_page(url,params)
