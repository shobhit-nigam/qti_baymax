import re

stra = "Harnaaz Sandhu"
pat = "Sandhu"

res = re.search(pat, stra)

if res:
    print("match")
else:
    print("no match")
