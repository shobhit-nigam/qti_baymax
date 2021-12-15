import csv

lista = ["num", "name", "spouse"]
listb = [1, "ranveer", "deepika"]
listc = [2, "katrina", "vicky"]
listd = [3, "salman", None]

listx = [lista, listb, listc, listd]

with open('actors.csv', 'w') as objf:
    objw = csv.writer(objf)
    objw.writerows(listx)
