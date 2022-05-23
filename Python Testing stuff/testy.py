tagsToBeExported = ['AZ900', 'DP900', 'AI900',
                    'PL300', 'DP203', 'PL900', 'customTag']

masterOp = []

for tag in tagsToBeExported:
    masterOp.append([])


masterOp[tagsToBeExported.index('AZ900')].append('Does this work')


print(masterOp)

if masterOp[1]:
    print("ye")
else:
    print("no")
