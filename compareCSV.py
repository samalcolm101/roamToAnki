import csv

# Name of the cert you are comparing
nameOfCert = "dp900"
op = []

# Opens the full library CSV
with open(f'{nameOfCert}_full.csv', 'r', encoding='UTF8') as csv1, open(f'{nameOfCert}.csv', 'r', encoding='utf-8-sig') as csv2:
    import1 = csv.reader(csv2)
    import2 = csv.reader(csv1)
    import1 = list(import1)
    import2 = list(import2)
    for row in import1:  # If question from new CSV isn't in the full library then append to OP list
        if row not in import2:
            op.append(row)

# Creates a list of just the differences
with open(f'{nameOfCert}_updates.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(op)
