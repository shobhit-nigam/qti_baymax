# objf = open("books.txt", "r")

with open("books.txt", "r") as objf:
    stra = objf.read()

lista = stra.splitlines()
print("lista =", lista)

#help(open)
