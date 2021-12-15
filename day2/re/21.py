import re

with open("log.txt", "r") as fa:
    stra = fa.read()

pat = "[\s][\S]*[2-9]$"
res = re.findall(pat, stra)
print(res)
