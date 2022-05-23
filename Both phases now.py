# Imports
from email.encoders import encode_noop
import json
import csv
import os.path

# OP lists

tagsToBeExported = ['AZ900', 'DP900', 'AI900',
                    'PL300', 'DP203', 'PL900', 'Deprecated']

masterOp = []

for tag in tagsToBeExported:
    masterOp.append([])


def appendToOpLists(tags, parent, question):
    for tag in tagsToBeExported:
        if tag in tags.upper():
            masterOp[tagsToBeExported.index(tag)].append(
                [question, parent['title'], tags])


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
    for tag in tagsToBeExported:
        if masterOp[tagsToBeExported.index(tag)]:
            with open(f"{tag}-export-new.csv", 'w', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(masterOp[tagsToBeExported.index(tag)])


def compareCSV():
    for tag in tagsToBeExported:
        comparisonOP = []
        if masterOp[tagsToBeExported.index(tag)]:
            try:
                with open(f'{tag}-export-old.csv', 'r', encoding='UTF8') as csv1, open(f'{tag}-export-new.csv', 'r', encoding='utf-8-sig') as csv2:
                    import1 = csv.reader(csv2)
                    import2 = csv.reader(csv1)
                    import1 = list(import1)
                    import2 = list(import2)
                    for row in import1:  # If question from new CSV isn't in the full library then append to OP list
                        if row not in import2:
                            comparisonOP.append(row)
                with open(f'{tag}-updates.csv', 'w', encoding='UTF8', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(comparisonOP)
            except Exception as e:
                print(f"There was a comparison error: {e}")


f = open('17MAYDP900concepts.json', encoding="utf8")

data = json.load(f)  # Load the JSON file

try:
    getParents(data)
    compareCSV()
except Exception as e:
    print("There was a master error: {e}")
print("\n Completed\n")
