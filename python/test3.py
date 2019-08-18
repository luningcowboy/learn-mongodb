import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myclient['runoobdb']
mycol = mydb['sites']
mylist = [
        {"_id": 1,"name":"Taobao","alexa": "100", "url":"https://www.taobao.com"},
        {"_id": 2,"name":"QQ","alexa": "100", "url":"https://www.qq.com"},
        {"_id": 3,"name":"Facebook","alexa": "100", "url":"https://www.facebook.com"},
        {"_id": 4,"name":"知乎","alexa": "100", "url":"https://www.zhihu.com"},
        {"_id": 5,"name":"Github","alexa": "100", "url":"https://www.github.com"}
        ]
x = mycol.insert_many(mylist)
print(x.inserted_ids)
