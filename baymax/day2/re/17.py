import re

stra = "mr.nigam@gmail.org angu@qti.qualcomm.com mr.nigam@gmail"
pat = "^([a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.)(com|org)"

res = re.findall(pat, stra)
print(res)
