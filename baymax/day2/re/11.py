import re

with open("avengers.txt", "r") as objf:
    stra = objf.read()

pat = ":"
rep = "  "
res = re.subn(pat, rep, stra)
print(res)

"""
res = re.match(pat, stra)

obj = re.compile(pat)
res = obj.match(stra)
"""
