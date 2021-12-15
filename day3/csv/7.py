import csv
with open('actors.csv', 'r') as objf:
    objr = csv.DictReader(objf)

    for x in objr:
        print(dict(x))
