import requests
res = requests.get('http://bj.xiaozhu.com/')#网站为小猪短租网北京地区网址
print(res)
#pycharm中返回结果为<Response [200]>，说明请求网址成功，若为404,400则请求网址失败。
print(res.text)
