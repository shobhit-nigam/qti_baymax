import re

with open("data.txt", "r") as objf:
    stra = objf.read()

pattern = "[0-9]{4}"
res = re.findall(pattern, stra)

print(res)
