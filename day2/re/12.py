import re

stra = "Harnaaz Sandhu, miss_universe"
pat = "(\w+) (\w+)"

res = re.match(pat, stra)

print(res)

print(res.group(0))
print(res.group(1))
print(res.group(2))

# error
#print(res.group(3))
