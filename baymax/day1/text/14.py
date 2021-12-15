with open("data.txt", "r") as objf:
    stra = objf.read()

lista = stra.splitlines()

list_col = []

for line in lista:
    list_col.append(int(line.split()[1]))


print(list_col)
