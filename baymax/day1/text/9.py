# objf = open("books.txt", "r")

with open("books.txt", "r") as objf:
    stra = objf.readlines()

print("type(stra) =", type(stra))
print("stra =", stra)
