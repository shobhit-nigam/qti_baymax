import json

dicta = '{"aa":20, "bb":30, "ff":55}'

json_obj = json.loads(dicta)

print(type(json_obj))
print(json.dumps(json_obj, indent = 4))
