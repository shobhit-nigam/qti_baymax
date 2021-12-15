import xml.etree.ElementTree as ET

tree_a = ET.parse('books.xml')
root_a = tree_a.getroot()

for x in root_a:
    stra = x.find('title').text
    strb = x.find('price').text
    print(stra, "\t", strb)
