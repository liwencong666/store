import random
from DBUtils import update
from DBUtils import select


f = open(file="古诗.txt",mode="r+",encoding="utf-8")
data = f.readlines()
sql = "insert into user values(%s,%s,%s)"
for index,i in enumerate(data):
    da = i.replace("\n","").split(",")
    update(sql,da)
sql1="select  sum(净资产) from  user"
money=select(sql1,[])
print(money[0][0])



















