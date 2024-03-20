# XML Translation Task

## Overview
This Python script translates text content from English (en-US) to Canadian French (fr-CA) within an XML file. It utilizes the `xml.etree.ElementTree` module for XML parsing and the `mtranslate` library for language translation.

## Usage
1. Ensure Python is installed on your system.
2. Install the required dependencies using pip:

```bash
pip install mtranslate==1.8
```

3. Set up python virtual environment for the project.

4. Run the script by executing:
```bash
python translate_xml.py
```

5. The script will load an XML file named `sheet.xml`, find text content under `<en-US>` tags, translate it to Canadian French, and update the corresponding `<fr-CA>` tags.
6. A new XML file named `modified_sheet.xml` will be generated with the translated content.

## Requirements
- Python 3.x
- mtranslate==1.8

## Files
- `translate_xml.py`: Python script for translating XML content.
- `sheet.xml`: Input XML file with English text to translate.
- `modified_sheet.xml`: Output XML file with translated Canadian French text.

## Note
- The script is meant to be used for translation from ENUS to CAFR, but is customizable to meet 
  different needs. Ensure that the input XML file (`sheet.xml`) has `<en-US>` and `<fr-CA>` tags for the 
  script to work correctly is used as it is.
