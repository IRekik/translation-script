import xml.etree.ElementTree as ET
import mtranslate as mt

# Specify which file to translate
xml_file = 'sheet.xml'

# Parse the XML file
tree = ET.parse(xml_file)
root = tree.getroot()

# For each Item tag, apply transformation
for item in root.findall('Item'):
    # Find the <en-US> and <fr-CA> tags under each <Item> element
    en_us_tag = item.find('en-US')
    fr_ca_tag = item.find('fr-CA')
    if (en_us_tag and fr_ca_tag) is not None:
        # Uses mtranslate library to translate from enUS to frCA
        translated_text = mt.translate(en_us_tag.text, 'fr', 'ca')
        fr_ca_tag.text = translated_text

# Produces a new document with modifications
tree.write('modified_sheet.xml', encoding='utf-8', xml_declaration=True)

print("Modified XML saved to 'modified_sheet.xml'")
