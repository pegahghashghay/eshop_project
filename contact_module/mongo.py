import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


def contact_us(name, email, masseg, title):
    mydict = {"name": name,
              "email": email,
              "message": masseg,
              "title": title}
    x = mycol.insert_one(mydict)
    # newvalues = {"$set":
    #                  "name": name,
    #                  "email": email,
    #                  "message": masseg,
    #                  "title": title}
    # mycol.update_one(mydict, newvalues)
    # for x in mycol.find():
    #     print(x)


def profille(full_name, massseg):
    mydict = {"name": full_name,
              "email": massseg}
    x = mycol.insert_one(mydict)