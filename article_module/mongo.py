import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


def listview(select):
    mydict = {"choose": select}
    mycol.insert_one(mydict)


def detailview(massege):
    myquery = {"name": massege}
    mycol.insert_one(myquery)
