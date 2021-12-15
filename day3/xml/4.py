import xml.etree.ElementTree as ET

tree_a = ET.parse('books.xml')
root_a = tree_a.getroot()

for x in root_a[0]:
    print(x.tag, x.attrib, x.text)
