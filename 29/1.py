#post提交表单
import requests
params = {
    'key1':'value1',
    'key2':'value2',
    'key3':'value3',
}

html = requests.post(url,data=params)
print (html.text)