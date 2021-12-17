import configparser

objc = configparser.ConfigParser()
objc.read('config.ini')
list_sec = objc.sections()

for s in list_sec:
    print("Section =", s)
    for k, v in objc.items(s):
        print(k,":\t", v)
    print("----")
