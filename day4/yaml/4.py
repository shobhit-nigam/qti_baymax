#pyaml
import yaml

with open('data1.yaml') as objf:
    data = yaml.load_all(objf, Loader=yaml.FullLoader)

    for doc in data:
        print("document -->")
        for k, v in doc.items():
            print(k, ":", v)
        print()
