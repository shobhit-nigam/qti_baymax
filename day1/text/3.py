objf = open("books.txt", "r")

stra = objf.read(5)
print("stra =", stra)
#print(type(stra))
print("---")
stra = objf.read(6)
print("stra =", stra)
objf.close()
