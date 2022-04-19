import json
import csv

az900 = []
dp900 = []
ai900 = []


def removeHashTags(text):
    text = text.replace('[', '').replace(']', '').replace(
        '>', '').replace('"', '')
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
            question = question.split()
            question = " ".join(question)
            if "AZ900" in tags:
                az900.append([question, parent['title'], tags])
            if "DP900" in tags:
                dp900.append([question, parent['title'], tags])
            if "AI900" in tags:
                ai900.append([question, parent['title'], tags])


def getParents(jsonObj):
    for items in jsonObj:
        try:
            if len(items["children"]) > 0:
                getChildren(items)
        except:
            continue
    createCSV()


def createCSV():
    with open('az900.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(az900)
    with open('dp900.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(dp900)
    with open('ai900.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(ai900)


f = open('1140DP900concepts.json', encoding="utf8")

data = json.load(f)

print("Running")
getParents(data)
print("\n Done")
