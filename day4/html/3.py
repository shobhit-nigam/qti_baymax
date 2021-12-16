import requests
from bs4 import BeautifulSoup

url = "https://www.qualcomm.com/"

objr = requests.get(url)
objh = objr.text

objs = BeautifulSoup(objh, "html5lib")

#print(objs.title)
print(objs.title.string)
