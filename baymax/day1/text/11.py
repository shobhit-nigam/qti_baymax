# objf = open("books.txt", "r")

with open("books.txt", "r") as objf:
    lista = objf.readlines()

objg = open("books_b.txt", "w")

for line in lista:
    if 't' in line:
        objg.write(line)

objg.close()
