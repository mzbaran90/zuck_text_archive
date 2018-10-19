import os
import csv
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

os.chdir('/Users/MasonBaran/Desktop')

filenames = '2018.075.txt'


def csv_metadata():

    listofdict= []
    fieldnames = ['record_id', 'participants', 'type', 'format', 'date', 'source', 'title', 'description']

    with open('zuckerberg.csv', 'r', encoding='utf-8') as infile:

        reader = csv.DictReader(infile, fieldnames)
        for row in reader:
            metadata = {}
            for name in fieldnames:
                metadata[name] = row[name]

            listofdict.append(metadata)
        return listofdict


##this assigns sub elements to the metadata element from the list of record dictionary
def xml_create_metadata(listofdicts):
    for dict in listofdicts:
        root = ET.Element('transcript')
        for key, value in dict.items():
            if key == 'record_id':
                record_id = ET.SubElement(root, key)
                record_id.text = value
            if key =='participants':
                participants = ET.SubElement(root, key)
                participants.text = value
            if key == 'type':
                record_type = ET.SubElement(root, key)
                record_type.text = value
            if key == 'format':
                record_format = ET.SubElement(root, key)
                record_format.text = value
            if key =='date':
                date = ET.SubElement(root,key)
                date.text = value
            if key == 'source':
                source = ET.SubElement(root, key)
                source.text = value
            if key == 'title':
                title = ET.SubElement(root, key)
                title.text = value
            if key == 'description':
                description = ET.SubElement(root, key)
                description.text = value




        xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
        return xmlstr















def main():
    listofdict = csv_metadata()
    xml_create_metadata(listofdict)



main()












