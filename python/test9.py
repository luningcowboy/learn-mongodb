import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myclient['runoobdb']
mycol = mydb['sites']

myquery = {"name":{"$regex":"^F"}}
x = mycol.delete_many(myquery)
print(x.deleted_count,"个文档已经删除")
print(x)
