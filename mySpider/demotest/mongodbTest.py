#!/usr/bin/python3

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["demo"]
mycol = mydb["spider2"]

x = mycol.find_one()

print(x)

mycol.insert_one({"name": "guikun"})

x = mycol.find_one()

print(x)
