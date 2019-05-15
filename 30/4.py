#读取csv文件 每行数据转化为list
#第一行作为字典格式的键 其余行作为值
import csv
fp = open('QQmail.csv',encoding='utf-8')
reader = csv.DictReader(fp)
for row in reader:
    print (row)
fp.close()