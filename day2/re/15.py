import re

stra = "mr.nigam@gmail.com sends a mail to angu@qti.qualcomm.com"
pat = "\S+@\S+"

res = re.findall(pat, stra)
print(res)
