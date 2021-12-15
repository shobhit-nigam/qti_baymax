import xml.etree.ElementTree as ET

tree_a = ET.parse('books.xml')
root_a = tree_a.getroot()

for x in root_a:
    strb = str(round(float(x.find('price').text)*1.05, 2))
    x.find('price').text = strb
    # local object
    x.set('updated', 'yes')

tree_a.write('new_books.xml')


help(x.set)
