stra = input()

print("stra =", stra)

import re

pattern = "^h..l"
res = re.match(pattern, stra, re.IGNORECASE)

if res:
    print("found hell")
else:
    print("only heaven")
