"""
数据库读操作演示
select
"""

import pymysql

#　创建连接
db = pymysql.connect(host='localhost',
                     user='root',
                     passwd = "123456",
                     database='stu',
                     charset='utf8')

#　创建游标
cur = db.cursor()

sql  = "select * from myclass where age=13;"

#　执行语句 cur拥有查询结果
cur.execute(sql)

#　获取查找结果的第一个
# one_row = cur.fetchone()
# print(one_row)

# 获取从查找结果前２个
# many_row = cur.fetchmany(2)
# print(many_row)

#　获取全部查询结果
all_row = cur.fetchall()
print(all_row)

cur.close()
db.close()










