from pymongo import MongoClient

import csv

op = []

cluster = MongoClient(
    "mongodb+srv://admin:admin@cluster0.eg4ik.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


db = cluster["roamData"]
collection = db["forss"]


def removeHashTags(text):
    text.replace('[', '').replace(']', '')
    partition = text.partition("#")
    question = partition[0]
    withouthash = partition[-1].replace('QuizQuestion', "")
    tags = withouthash.replace('#', '').split()
    tags = ','.join(tags)
    return question, tags


for x in collection.find():
    for y in x["children"]:
        if "#QuizQuestion" in y["string"]:
            question, tags = removeHashTags(y["string"])
            op.append([question, x['title'], tags])

with open('anki.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(op)

print("done\n")