import csv

with open('data.csv', 'r') as objf:
    objr = csv.reader(objf, delimiter = ' ')

    for x in objr:
        print(x[1])
