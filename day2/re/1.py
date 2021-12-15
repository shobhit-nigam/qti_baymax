stra = input()

print("stra =", stra)

import re

pattern = "hell"
res = re.match(pattern, stra)

if res:
    print("found hell")
else:
    print("only heaven")
