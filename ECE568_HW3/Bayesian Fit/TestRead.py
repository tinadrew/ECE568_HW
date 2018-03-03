"""
f = open('AMZN_history.csv', 'rb')
csv_f = csv.reader(f)
data = []
for row in csv_f:
    rows = float(row[5])
    data.append(rows)
print (data)
f.close()
"""
data = []
data1 = []

'''Code from: https://docs.python.org/3/library/csv.html'''
import csv
import numpy as np
x = np.array(['1.1', '2.2', '3.3'])
y = x.astype(np.float)

with open('AMZN_history.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        #rows = float(row[4])
        #data.append(rows)
        print(', '.join(row))
        data.append(', '.join(row))
        #[float(i) for i in row]


import csv
data1 = []
def readLines():
    with open('AMZN_history-.csv', 'rU') as data:
        reader = csv.reader(data)
        row = list(reader)
        for x in row:
            data1.append([float(str(y)) for y in x])
            print(data1)
readLines()