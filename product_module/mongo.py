import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]



def product_list(title,price):
    mydict = {"name": title,
              "price": price}
    mycol.insert_one(mydict)



def product_detail(title,price):
    mydict = {"name": title,
              "price": price}
    mycol.insert_one(mydict)



def product_favorite(title):
    mydict = {"name": title}
    mycol.insert_one(mydict)
