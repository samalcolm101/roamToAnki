import csv

nameOfCert = "az900"
op = []

with open(f'{nameOfCert}_full.csv', 'r', encoding='UTF8') as csv1, open(f'{nameOfCert}.csv', 'r', encoding='UTF8') as csv2:
    import1 = csv.reader(csv1)
    import2 = csv.reader(csv2)
    for row in import1:
        if row not in import2:
            op.append(row)

with open(f'{nameOfCert}_updates.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(op)