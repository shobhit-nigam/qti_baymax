import re

with open("avengers.txt", "r") as objf:
    stra = objf.read()

pat = ":"
res = re.split(pat, stra, 2)
print(res)
