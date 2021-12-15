import re

with open("log.txt", "r") as fa:
    lista = fa.readlines()

pat = "[2-9]+\n$"
for line in lista:
    if re.findall(pat, line):
        print(line)
