import re

stra = "Harnaaz Sandhu, miss_universe"
pat = "(?P<first_name>\w+) (?P<second_name>\w+), (?P<title>\w+)"

res = re.match(pat, stra)

dicta = res.groupdict()

print(dicta)
