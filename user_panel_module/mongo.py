import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

def user_panel_dashbord(name):
    mydict = {"name": name}
    x = mycol.insert_one(mydict)



def edit_user_panel(about_user, address):
    myquery = {"name": about_user,
              "address": address}
    newvalues = { "$set": { "name": about_user,
              "address": address } }
    mycol.update_one(myquery, newvalues)



def change_password(password):
    myquery = {"password": password}
    newvalues = { "$set": { "password": password} }
    mycol.update_one(myquery, newvalues)