import json
from pymongo import MongoClient


cluster = MongoClient(
    "mongodb+srv://admin:admin@cluster0.eg4ik.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


db = cluster["roamData"]
collection = db["forss"]


# collection.insert_one()


# Opening JSON file
f = open('1840DP900concepts.json', encoding="utf8")

# returns JSON object as
# a dictionary
data = json.load(f)

x = 1


for items in data:
    try:
        if len(items["children"]) > 0:
            print(len(items["children"]))
            collection.insert_one(items)
    except:
        continue


# collection.insert_one(items)
