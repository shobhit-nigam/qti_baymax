with open("data.txt", "r") as objf:
    stra = objf.read()

lista = stra.splitlines()

# comprehension 
list_col = [int(line.split()[1]) for line in lista]
print(list_col)
