import re

with open("data.txt", "r") as objf:
    stra = objf.read()

pattern = "\d{4}"
res = re.findall(pattern, stra)

print(res)
