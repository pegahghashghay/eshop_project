import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


def sinin(username, created_date):
    mydict = {"name": username,
              "Time": created_date}
    mycol.insert_one(mydict)


def Log_out(username, created_date):
    myquery = {"name": username,
               "Time": created_date}
    mycol.delete_one(myquery)
