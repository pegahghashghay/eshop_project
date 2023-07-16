import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


def contact_us(email, masseg):
    mydict = {"email": email,
              "message": masseg}
    x = mycol.insert_one(mydict)


def creatprofille(full_name, email):
    mydict = {"name": full_name,
              "email": email}
    x = mycol.insert_one(mydict)



