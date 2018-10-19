import os
import csv
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import glob

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
                    print('test')
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
def content_test(single_file):

    line_list = []
    index = 0
    single_file_with_ext = single_file + '.txt'
    with open(single_file_with_ext, 'r', encoding='utf-8') as inFile:
        for line in inFile.readlines():
            index += 1
            if line.isspace():
                index -= 1

            if not line.isspace():
                line_list.append(line)
                if line.__contains__('##content##'):
                    pos = index

    line_list = line_list[pos:]  # line_list is now comprised of everything ##contents## on
    print(line_list)

def main():
    files_no_ext = [file.split('.')[0] for file in getfiles()]  # trims file extension so csv record_id can be parsed
    listofdict = csv_metadata(files_no_ext)
    for single_file in files_no_ext:
        metadata = xml_create_metadata(listofdict, single_file)
        content =




main()












