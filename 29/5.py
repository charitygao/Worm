#jieba库词频统计
""" import jieba.analyse
tags = jieba.analyse.extract_tags(content,topK=num,withWeight=True)
for item in tags:
    print (item[0],item[1]) """

import jieba.analyse
path = "../doupo.txt"
fp = open(path,'r')
content = fp.read()
try:
    jieba.analyse.set_stop_words('中文停用词表.txt')
    tags = jieba.analyse.extract_tags(content,topK=100,withWeight=True)
    for item in tags:
        print(item[0]+'\t'+str(int(item[1]*1000)))
finally:
    fp.close()
