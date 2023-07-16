import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


def listview(title, date):
    mydict = {"name": title,
              "creattime": date}
    mycol.insert_one(mydict)


def comment(massege):
    myquery = {"massege": massege}
    mycol.insert_one(myquery)
