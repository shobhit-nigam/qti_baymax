import configparser

objc = configparser.ConfigParser()
objc.read('config.ini')

print(objc.sections())
