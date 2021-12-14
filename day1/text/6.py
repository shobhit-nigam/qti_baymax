objf = open("books.txt", "r")

help(objf.seek)

objf.read(11)
objf.seek(8, 2)
    # jump 8 bytes form current
stra = objf.read(4)
print("stra =", stra)
# lseek, fseek
