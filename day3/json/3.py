import json

with open("example_2.json", "r") as objj:
    data = json.load(objj)


def get_data(d):
    for k, v in d.items():
        if type(v) is dict:
            get_data(v)
        else:
            print(k, ":")
            print(v)
            print("-----")

get_data(data)
