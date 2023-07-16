import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


def sinin(username, created_date):
    mydict = {"name": username,
              "Time": created_date}
    mycol.insert_one(mydict)

def forget(passs, email):
    myquery = {"name": passs,
               "email": email}
    mycol.delete_one(myquery)

def rejester(passs, email):
    myquery = {"name": passs,
               "email": email}
    mycol.delete_one(myquery)


def reset(passs, email):
    myquery = {"name": passs,
               "email": email}
    mycol.delete_one(myquery)


def Log_out(username, email):
    myquery = {"name": username,
               "email": email}
    mycol.delete_one(myquery)