import re

stra = "Harnaaz Sandhu, miss_universe"
pat = "(?P<first_name>\w+) (?P<second_name>\w+), (?P<title>\w+)"

res = re.match(pat, stra)

print(res.group(1))
print(res.group(2))
print(res.group(3))
print("----")
print(res.group('first_name'))
print(res.group('second_name'))
print(res.group('title'))
