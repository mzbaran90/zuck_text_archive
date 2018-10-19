''' This program converts the old Zuckerberg txt transcripts to xml files.
Metadata is grabbed from the Zuck Master Files Source.csv while the contents are parsed from the txt transcripts themselves'''

import os
import glob
import csv
import xml.etree.ElementTree as ET


os.chdir('/Users/MasonBaran/Desktop/zuck_stuff/zuck_text_archive/txt_content')

#returns files with appropriate extensions

def getfiles():
    filenames = list(glob.glob('*.txt'))
    return filenames


#Gather relevant csv rows (as dictionaries) based of filesnoext parameter
def gathercsvmetadata(filesnoext):

    list_of_records= [] # list of dictionaries - each dictionary represents a record
    fieldnames = ['record_id', 'participants', 'type', 'format', 'date', 'source', 'title', 'description']

    with open('zuckerberg.csv', 'r', encoding='utf-8') as infile:

        reader = csv.DictReader(infile, fieldnames)
        for row in reader:
            metadata = {}
            for name in fieldnames:
                metadata[name] = row[name]

            list_of_records.append(metadata)
def xml_builder(list_of_records, ):
    for record in list_of_records:



def main():
    files_no_ext = [file.split('.')[0] for file in getfiles()] #trims file extension so csv record_id can be parsed
    csv_metadata = gathercsvmetadata(files_no_ext) #returns objects storing dictionaries







