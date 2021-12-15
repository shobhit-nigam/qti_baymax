import xml.etree.ElementTree as ET

tree_a = ET.parse('books.xml')
root_a = tree_a.getroot()

ET.SubElement(root_a[1], 'kindle')
ET.SubElement(root_a[4], 'kindle')

for x in root_a.iter('kindle'):
    x.text = "available for kindle"

tree_a.write('ebooks.xml')
