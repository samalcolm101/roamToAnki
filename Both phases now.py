# Imports
import json
import csv

# OP lists
az900 = []
az900Deprecated = []
dp900 = []
dp900Deprecated = []
ai900 = []
ai900Deprecated = []
pl300 = []
pl300Deprecated = []
dp203 = []
dp203Deprecated = []
pl900 = []
pl900Deprecated = []
x = 1


def appendToOpLists(tags, parent, question):

    if "AZ900" in tags.upper():
        if "Deprecated" in tags:
            az900Deprecated.append(
                [question, parent['title'], tags])
        else:
            az900.append([question, parent['title'], tags])
    if "DP900" in tags.upper():
        if "Deprecated" in tags:
            dp900Deprecated.append(
                [question, parent['title'], tags])
        else:
            dp900.append([question, parent['title'], tags])
    if "AI900" in tags.upper():
        if "Deprecated" in tags:
            ai900Deprecated.append(
                [question, parent['title'], tags])
        else:
            ai900.append([question, parent['title'], tags])
    if "PL300" in tags.upper():
        if "Deprecated" in tags:
            pl300Deprecated.append(
                [question, parent['title'], tags])
        else:
            pl300.append([question, parent['title'], tags])
    if "DP203" in tags.upper():
        if "Deprecated" in tags:
            dp203Deprecated.append(
                [question, parent['title'], tags])
        else:
            dp203.append([question, parent['title'], tags])
    if "PL900" in tags.upper():
        if "Deprecated" in tags:
            pl900Deprecated.append(
                [question, parent['title'], tags])
        else:
            pl900.append([question, parent['title'], tags])

# Splits a text object into its question and answer


def splitQandA(text):  # TODO get tags
    quenswer = text.partition('#')[2]
    splitQuenswer = quenswer.partition('#')
    question = splitQuenswer[0].replace("Question", "")
    question = question
    question = question.split()
    question = " ".join(question)
    answer = splitQuenswer[-1].replace("Answer", "")
    answer = answer
    answer = answer.split()
    answer = " ".join(answer)
    return(question, answer)


# Splits a text object into its question part and its tag part
def removeHashTags(text):
    text = text.replace('[', '').replace(']', '').replace(
        '>', '').replace('"', '')  # removes any punctuation
    partition = text.partition("#")  # splits question from tags
    question = partition[0]
    withouthash = partition[-1].replace('QuizQuestion', "")
    # removes the #s from the list of tags
    tags = withouthash.replace('#', '').split()
    tags = ','.join(tags)  # inserts a comma so it can be joined as a list
    return question, tags


# Splits children from a parent object
def getChildren(parent):
    for y in parent["children"]:
        # Splits QuizQuestions apart from other children
        if "#quizquestion" in y["string"].lower():
            question, tags = removeHashTags(y["string"])
            question = question.split()
            question = " ".join(question)
            parent['title'] = parent['title'].replace('[', '').replace(']', '').replace(
                '>', '').replace('"', '')
            if parent["title"] == "Example Page":
                continue
            else:
                appendToOpLists(tags, parent, question)


# Splits parents (including children) from the JSON OBJ
def getParents(jsonObj):
    for items in jsonObj:
        try:
            if len(items["children"]) > 0:
                getChildren(items)
        except:
            continue  # Ignore if it doesn't have children
    createCSV()


# Creates the CSVs from the OP lists
def createCSV():
    if az900:
        with open('az900.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(az900)
    if az900Deprecated:
        with open('az900Deprecated.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(az900)
    if dp900:
        with open('dp900.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(dp900)
    if dp900Deprecated:
        with open('dp900Deprecated.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(dp900Deprecated)
    if ai900:
        with open('ai900.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(ai900)
    if ai900Deprecated:
        with open('ai900Deprecated.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(ai900Deprecated)
    if pl300:
        with open('pl300.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(pl300)
    if pl300Deprecated:
        with open('pl300Deprecated.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(pl300Deprecated)
    if dp203:
        with open('dp203.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(dp203)
    if dp203Deprecated:
        with open('dp203Deprecated.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(dp203Deprecated)
    if pl900:
        with open('pl900.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(pl900)
    if pl900Deprecated:
        with open('pl900Deprecated.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(pl900Deprecated)


f = open('17MAYDP900concepts.json', encoding="utf8")

data = json.load(f)  # Load the JSON file

print("Running")
getParents(data)
print("\n Done")
