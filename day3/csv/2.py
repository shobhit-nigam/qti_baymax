import csv

with open('data1.csv', 'r') as objf:
    objr = csv.reader(objf)
    print(type(objr))
