import json
import csv

op = []

def removeHashTags(text):
    text.replace('[', '').replace(']', '')
    partition = text.partition("#")
    question = partition[0]
    withouthash = partition[-1].replace('QuizQuestion', "")
    tags = withouthash.replace('#', '').split()
    tags = ','.join(tags)
    return question, tags


def getChildren(parent):
    for y in parent["children"]:
        if "#QuizQuestion" in y["string"]:
            question, tags = removeHashTags(y["string"])
            op.append([question, parent['title'], tags])


def getParents(jsonObj):
    for items in jsonObj:
        try:
            if len(items["children"]) > 0:
                getChildren(items)
        except:
            continue
    createCSV()


def createCSV():
    with open('anki.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(op)


f = open('1840DP900concepts.json', encoding="utf8")

data = json.load(f)

print("Running")
getParents(data)
print("\n Done")