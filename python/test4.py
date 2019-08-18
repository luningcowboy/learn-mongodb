import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myclient['runoobdb']
mycol = mydb['sites']
# 随机一条
x = mycol.find_one()
print(x)
# 查询所有
for x in mycol.find():
    print(x)
# 查询指定字段的数据
print("******************")
# find 用来查询指定字段的数据， 将要返回的字段设置为1
for x in mycol.find({},{"_id": 0, "name":1, "alexa": 1}):
    print(x)

print("******************")
# find 用来查询指定字段的数据， 将要返回的字段设置为1
# 除了_id你不能在一个对象中同时指定0和1， 如果你设置了一个字段为0，则其他字段都为1， 反之亦然
# 下面的例子是排除了alexa字段
for x in mycol.find({},{"alexa": 0}):
    print(x)
# 同时指定0和1 会报错
"""
for x in mycol.find({},{"name":1,"alexa": 0}):
    print(x)
"""
# 根据指定条件查询
print("******************")
myquery = {"name":"runoob"}
mydoc = mycol.find(myquery,{"alexa":0})
for x in mydoc:
    print(x)
# 高级查询
print("******************")
# 读取name字段中第一个字母ASCII值大于"H"的数据,大于的修饰符条件为{"$gt":"H"}
myquery = {"name":{"$gt":"H"}}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)
