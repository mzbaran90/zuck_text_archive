import os
import csv
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import glob
import Contents_Class

os.chdir('/Users/MasonBaran/Desktop/zuck_txt_testing')

filenames = ['2018.075.txt', '2009-003.txt', '2016-065.txt']


def getfiles():
    filenames = list(glob.glob('*.txt'))
    return filenames


def csv_metadata(filenames):

    listofdict= []
    fieldnames = ['record_id', 'participants', 'type', 'format', 'date', 'source', 'title', 'description']

    with open('zuckerberg.csv', 'r', encoding='utf-8') as infile:

        reader = csv.DictReader(infile, fieldnames)
        for row in reader:
            metadata = {}
            for filename in filenames:
                if row['record_id'] == filename:

                    for name in fieldnames:
                        metadata[name] = row[name]

                    listofdict.append(metadata)

        return listofdict


##this assigns sub elements to the metadata element from the list of record dictionary
def xml_create_metadata(listofdicts, filename):
    for dict in listofdicts:

        if dict['record_id'] == filename:
            root = ET.Element('transcript')

            for key, value in dict.items():
                if key == 'record_id':
                    record_id = ET.SubElement(root, key)
                    record_id.text = value
                if key == 'participants':
                     participants = ET.SubElement(root, key)
                     participants.text = value
                if key == 'type':
                    record_type = ET.SubElement(root, key)
                    record_type.text = value
                if key == 'format':
                    record_format = ET.SubElement(root, key)
                    record_format.text = value
                if key == 'date':
                    date = ET.SubElement(root, key)
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
            print(xmlstr)
            return xmlstr
        
def xml_create_content(content):
    root = ET.Element('content')
    for participant in content:
        for key, value in participant.items():
            key = ET.SubElement(root,'participant',attrib={'name': key})
            key.text = value
    xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
    print(xmlstr)
    return xmlstr

def main():
    files_no_ext = [file.split('.')[0] for file in getfiles()]  # trims file extension so csv record_id can be parsed

    listofdict = csv_metadata(files_no_ext)
#       cycles through each file and calls methods to build metadata and content 
    for single_file in files_no_ext:
        metadata = xml_create_metadata(listofdict, single_file)
        content_instance_create = Contents_Class.Contents(single_file)
        content = content_instance_create.content_creator()
        combined = xml_create_content(content)
        






main()












