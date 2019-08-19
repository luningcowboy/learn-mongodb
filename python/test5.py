import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017')
mdb = myclient['runoobdb']
mycol = mdb['sites']

myquery = {"alexa":10000}
newvalues = {"$set":{"alexa":"12345"}}
# update_one 只能修改一条记录
#mycol.update_one(myquery, newvalues)
# update_one 修改所有符合条件的记录
mycol.update_many(myquery, newvalues)

for x in mycol.find():
    print(x)
