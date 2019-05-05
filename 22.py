#mysql数据库的使用
import pymysql
conn = pymysql.connect(host='localhost',user='root',passwd='123456',db='mydb',port=3306,charset='utf8')
cursor = conn.cursor()
cursor.execute('insert into students (name,sex,grade) values(%s,%s,%s)',('张珊'，'女','67'))
conn.commit()