import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myclient['runoobdb']
mycol = mydb['sites']

mydoc = mycol.find().sort("alexa")
for x in mydoc:
    print(x)
print("倒序")
mydoc = mycol.find().sort("alexa",-1)
for x in mydoc:
    print(x)
