import re

with open("breakfast.txt", "r") as objf:
    stra = objf.read()

pattern = "dosa"
res = re.findall(pattern, stra)

if res:
    print("found dosa")
else:
    print("no dosa for me")
