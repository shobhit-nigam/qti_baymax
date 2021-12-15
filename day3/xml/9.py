import xml.etree.ElementTree as ET

tree_a = ET.parse('books.xml')
root_a = tree_a.getroot()

for x in root_a.iter('price'):
    x.text = str(round(float(x.text)*1.1, 2))
    x.set('updated', 'yes')

tree_a.write('new_books.xml')


help(x.set)
