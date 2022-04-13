text1 = '"These expenditures are generally nonrecurring and result in the acquisition of permanent assets" #QuizQuestion #AZ900_DescribeCloudConcepts'
text2 = '"These expenditures are generally nonrecurring and result in the acquisition of permanent assets" #AZ900_DescribeCloudConcepts #QuizQuestion'
text3 = '"These expenditures are generally nonrecurring and result in the acquisition of permanent assets" #AZ900_DescribeCloudConcepts #tag3 #QuizQuestion'
text4 = '"These expenditures are generally nonrecurring and result in the acquisition of permanent assets" #tag3 #AZ900_DescribeCloudConcepts #QuizQuestion'


def removeHashTagsAndShiz(text):
    partition = text.partition("#")
    question = partition[0]
    withouthash = partition[-1].replace('QuizQuestion', "")
    tags = withouthash.replace('#', '').split()
    return question, tags


Qs, tags = removeHashTagsAndShiz(text4)

print(Qs)
print(tags)
