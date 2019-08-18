import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myclient['runoobdb']
mycol = mydb['sites']
mydict = {"name":"runoob","alexa":10000, "url": "https://www.runoob.com"}
x = mycol.insert_one(mydict)
print(x)
print(x.inserted_id)

