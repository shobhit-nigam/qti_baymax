import configparser

objc = configparser.ConfigParser()
objc.read('config.ini')
list_sec = objc.sections()

for s in list_sec:
    print("Section =", s)
    print(objc.options(s))
    print("----")
