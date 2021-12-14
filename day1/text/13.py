with open("data.txt", "r") as objf:
    stra = objf.read()

lista = stra.splitlines()

list_col = []

for line in lista:
    temp = line.split()
    list_col.append(int(temp[1]))



print(list_col)
