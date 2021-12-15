import json

with open("example_1.json", "r") as objj:
    data = json.load(objj)

print(data)
print(data['fruit'])
