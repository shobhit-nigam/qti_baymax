# objf = open("books.txt", "r")

with open("books.txt", "r") as objf:
    stra = objf.read()

print("stra =", stra)

print(objf.closed)
