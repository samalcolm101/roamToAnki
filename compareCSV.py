#import pandas as pd
import csv

nameOfCert = "az900"
op = []

with open(f'{nameOfCert}_full.csv', 'r', encoding='UTF8') as csv1, open(f'{nameOfCert}.csv', 'r', encoding='UTF8') as csv2:
    import1 = csv.reader(csv1)
    import2 = csv.reader(csv2)
    for row in import1:
        if row not in import2:
            print(row)
            op.append(row)

with open(f'{nameOfCert}_updates.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(op)


# print(import1)


# with open('data_diff.csv', 'w') as outFile:         # Create CSV file with differences
# for row in import2:
#    if row not in import1:
#        print(row)
#        outFile.write(row)
