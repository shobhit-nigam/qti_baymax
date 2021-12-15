import xml.etree.ElementTree as ET

tree_a = ET.parse('books.xml')
root_a = tree_a.getroot()

print(root_a.tag)
print(root_a.attrib)
