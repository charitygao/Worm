#MongoDB的使用
import pymongo
#'example.com',username='user',password='password',authSource='the_database',authMechanism='SCRAM-SHA-1'
client = pymongo.MongoClient('localhost',27017,username='admin',password='123456') #连接数据库
mydb = client['mydb'] #新建mydb数据库
test = mydb['test'] #新建test数据集合
test.insert_one({'name':'Jan','sex':'男','grade':89}) #插入数据
#数据导出为csv mongoexport -d mydb -c test --csv -f name,sex,grade -o test.csv