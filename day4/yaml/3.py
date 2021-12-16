#pyaml
import yaml

with open('invoice.yaml') as objf:
    data = yaml.load(objf, Loader=yaml.FullLoader)

def get_data(d):
    for k, v in d.items():
        if type(v) is dict:
            get_data(v)
        else:
            print(k, ":")
            print(v)
            print("-----")

get_data(data)
