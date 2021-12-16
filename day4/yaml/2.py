#pyaml
import yaml

with open('data.yaml') as objf:
    data = yaml.load(objf, Loader=yaml.FullLoader)
    print(data['file_path'][1]['account'])
