import re

with open("avengers.txt", "r") as objf:
    stra = objf.read()

pat = ":"
rep = "\t"
res = re.sub(pat, rep, stra)
print(res)
