import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]




def generac(title, content):
    mydict = {"name": title,
              "text": content}
    mycol.insert_one(mydict)