import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017')
mdb = myclient['runoobdb']
mycol = mdb['sites']

myquery = {"name":{"$regex":"^F"}}
newvalues = {"$set":{"alexa":"123"}}

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "文档已经修改")
print(x)
