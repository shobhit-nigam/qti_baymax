import requests
from bs4 import BeautifulSoup
import re
from nltk.tokenize import RegexpTokenizer
import nltk

url = "https://en.wikipedia.org/wiki/Amitabh_Bachchan"

objr = requests.get(url)
objh = objr.text

objs = BeautifulSoup(objh, "html5lib")

#print(objs.title)
#print(objs.title.string)

temp = objs.get_text()

tokenizer = RegexpTokenizer('\w+')

objt = tokenizer.tokenize(temp)
words = []

for word in objt:
    words.append(word.lower())

# stop words
objs = nltk.corpus.stopwords.words('english')

new_words = []

for w in words:
    if w not in objs:
        new_words.append(w)

print(len(new_words))



import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

freq = nltk.FreqDist(new_words)
freq.plot(25)
