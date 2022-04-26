# Imports
import json
import csv

# OP lists
az900 = []
dp900 = []
ai900 = []

# Splits a text objcet into its question part and its tag part
def removeHashTags(text):
    text = text.replace('[', '').replace(']', '').replace(
        '>', '').replace('"', '') #removes any punctuation
    partition = text.partition("#") #splits question from tags
    question = partition[0]
    withouthash = partition[-1].replace('QuizQuestion', "")
    tags = withouthash.replace('#', '').split() #removes the #s from the list of tags
    tags = ','.join(tags) #inserts a comma so it can be joined as a list
    return question, tags

# Splits children from a parent object
def getChildren(parent):
    for y in parent["children"]:
        if "#QuizQuestion" in y["string"]: # Splits QuizQuestions apart from other children
            question, tags = removeHashTags(y["string"])
            question = question.split() # Removes any whitespace
            question = " ".join(question) 
            if "AZ900" in tags: #Appends all AZ900 questions
                az900.append([question, parent['title'], tags])
            if "DP900" in tags: #appends all DP900 questions
                dp900.append([question, parent['title'], tags])
            if "AI900" in tags: #appends all AI900 questions
                ai900.append([question, parent['title'], tags])

#splits parents (including children) from the JSON OBJ
def getParents(jsonObj):
    for items in jsonObj:
        try:
            if len(items["children"]) > 0: #if the parent has children
                getChildren(items)
        except:
            continue #Ignore if it doesnt have children
    createCSV()

#creates the CSVs from the OP lists
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
