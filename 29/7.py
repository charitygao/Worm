#爬取新浪微博好友圈信息
#词频统计
import jieba.analyse
path = 'weibo.txt'
fp = open(path,'r',encoding='utf-8')
content = fp.read()
try:
    jieba.analyse.set_stop_words('中文停用词表.txt')
    tags = jieba.analyse.extract_tags(content,topK=100,withWeight=True)
    for item in tags:
        print(item[0]+'\t'+str(int(item[1]*1000)))
finally:
    fp.close()