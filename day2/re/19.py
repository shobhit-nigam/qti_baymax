import re

stra = "nr.nigam@gmail.com sends an email to pbollam@qti.qualcomm.com and testmail@gmail.com"
pat = "[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.com" # should only have alphanumerics, _, ends with .com
pat = "[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.(com|org)" # should only have alphanumerics, _, ends with .com
res = re.findall(pat, stra)
print(res)
