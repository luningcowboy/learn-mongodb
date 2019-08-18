import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myclient['runoobdb']
mycol = mydb['sites']
mylist = [
        {"name":"Taobao","alexa": "100", "url":"https://www.taobao.com"},
        {"name":"QQ","alexa": "100", "url":"https://www.qq.com"},
        {"name":"Facebook","alexa": "100", "url":"https://www.facebook.com"},
        {"name":"知乎","alexa": "100", "url":"https://www.zhihu.com"},
        {"name":"Github","alexa": "100", "url":"https://www.github.com"}
        ]
x = mycol.insert_many(mylist)
print(x)
print(x.inserted_ids)
