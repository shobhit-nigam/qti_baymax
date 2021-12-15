with open("data1.csv", "r") as objf:
    stra = objf.read()

lista = stra.splitlines()

list_col = []

for line in lista:
    list_col.append(line.split(',')[2])


print(list_col)
