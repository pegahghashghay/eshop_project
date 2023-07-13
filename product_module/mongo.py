import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


def Product_Favorite(product, created_date):
    mydict = {"name": product,
              "Time": created_date}
    x = mycol.insert_one(mydict)
