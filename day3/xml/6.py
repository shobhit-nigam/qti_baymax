import xml.etree.ElementTree as ET

tree_a = ET.parse('books.xml')
root_a = tree_a.getroot()

objf = open("books.txt", "w")

for x in root_a:
    objf.write(x[1].text+'\n')
    objf.write(x[-1].text+'\n')
    objf.write("----------\n")

objf.close()
