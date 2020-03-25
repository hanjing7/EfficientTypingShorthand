import xml.etree.cElementTree as ET
import pandas as pd

file_name = "vocab.xlsx"
cols = ['original', 'abbr']
df = pd.read_excel(file_name, header=None, usecols=2, names=cols)
df.describe()
df.head()

plist = ET.Element("plist")
array = ET.SubElement(plist, "array")
for idx, row in df.iterrows():
#     print(row[cols[0]], row[cols[1]])
    entry = ET.SubElement(array, "dict")
    ET.SubElement(entry, "key").text = "phrase"
    ET.SubElement(entry, "string").text = row[cols[0]]
    ET.SubElement(entry, "key").text = "shortcut"
    ET.SubElement(entry, "string").text = row[cols[1]]
   
tree = ET.ElementTree(plist)
output = "jing_vocab.plist"

xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>'
doc_type = '<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">'

with open(output, 'wb') as f:
    f.write(f'{xml_declaration}\n{doc_type}\n'.encode('utf8'))
    tree.write(f, encoding='utf-8')

print("done!")