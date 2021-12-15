import re

with open("breakfast.txt", "r") as objf:
    stra = objf.read()

pattern = "dosa"
replace = "paratha"
res = re.sub(pattern, replace, stra)

print(res)
