import csv

with open('data1.csv', 'r') as objf:
    objr = csv.reader(objf)

    for x in objr:
        print(x[2])
