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

    list_of_records= []
    fieldnames = ['record_id', 'participants', 'type', 'format', 'date', 'source', 'title', 'description']

    with open('zuckerberg.csv', 'r', encoding='utf-8') as infile:

        reader = csv.DictReader(infile, fieldnames)
        for row in reader:
            metadata = {}
            for filename in filenames:
                if row['record_id'] == filename:

                    for name in fieldnames:
                        metadata[name] = row[name]

                    list_of_records.append(metadata)

        return list_of_records


##this assigns sub elements to the metadata element from the list of record dictionary
def xml_create_metadata(list_of_records, filename):
    for dict in list_of_records:

        if dict['record_id'] == filename:
            root = ET.Element('transcript')

            for key, value in dict.items():

                key = ET.SubElement(root, key)
                key.text = value

            xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
            return xmlstr
        
def create_xml_transcript(content):
    pass

def main():
    files_no_ext = [file.split('.')[0] for file in getfiles()]  # trims file extension so csv record_id can be parsed

    list_of_records = csv_metadata(files_no_ext)
#       cycles through each file and calls methods to build metadata and content 
    for single_file in files_no_ext:
        metadata = xml_create_metadata(list_of_records, single_file)
        content_instance_create = Contents_Class.Contents(single_file)
        content = content_instance_create.content_creator()



        






main()












