import configparser

objc = configparser.ConfigParser()
objc.read('config.ini')
list_sec = objc.sections()

for k, v in objc.items(list_sec[2]):
    print(k,":\t", v)
