#读取csv文件
import csv
fp = open('../doubanbook.csv')
reader = csv.reader(fp)
for row in reader:
    print (row)
fp.close()