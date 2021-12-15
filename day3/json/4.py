import json

dicta = {'aa':20, 'bb':30, 'ff':55}

with open("example_3.json", "w") as objj:
    json.dump(dicta, objj)
