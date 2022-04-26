import csv

#name of the cert you are comparing
nameOfCert = "az900"
op = []

#Opens the full library CSV
with open(f'{nameOfCert}_full.csv', 'r', encoding='UTF8') as csv1, open(f'{nameOfCert}.csv', 'r', encoding='UTF8') as csv2:
    import1 = csv.reader(csv1)
    import2 = csv.reader(csv2)
    for row in import1: #if question from new CSV isn't in the full library then append to OP list
        if row not in import2:
            op.append(row)

with open(f'{nameOfCert}_updates.csv', 'w', encoding='UTF8', newline='') as f: #Creates a list of just the differences
    writer = csv.writer(f)
    writer.writerows(op)