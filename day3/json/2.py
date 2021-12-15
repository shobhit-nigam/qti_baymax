import json

with open("example_2.json", "r") as objj:
    data = json.load(objj)

print(data)
print("-----")
print(data['quiz']['maths']['q2']['options'][1])
