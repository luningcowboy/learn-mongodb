import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myclient['runoobdb']
mycol = mydb['sites']

myquery = {"name":"Taobao"}

mycol.delete_one(myquery)
for x in mycol.find():
    print(x)
