import os
import glob
import csv
import Contents_Class
import XML_Builder

os.chdir('/Users/MasonBaran/Desktop/zuck_txt_testing')




def getfiles():
    filenames = list(glob.glob('*.txt'))
    return filenames

def list_csv_metadata(single_file):

    fieldnames = ['record_id', 'participants', 'type', 'format', 'date', 'source', 'title', 'description']

    with open('zuckerberg.csv', 'r', encoding='utf-8') as infile:

        reader = csv.DictReader(infile, fieldnames)
        for row in reader:
            metadata = {}

            if row['record_id'] == single_file:

                for name in fieldnames:
                    metadata[name] = row[name]

                return metadata

        


def main():
    files_no_ext = [file.split('.')[0] for file in getfiles()]  # trims file extension so csv record_id can be parsed


    for single_file in files_no_ext:

# creating instances of metadata and contents objects

        content_instance_create = Contents_Class.Contents(single_file)
        
# calling methods withing objects to build metadata and contents dictionaries
        metadata = list_csv_metadata(single_file)

        contents = content_instance_create.content_creator()


#   Creating instance of xml_transcript object
        xml_builder = XML_Builder.xml_builder(metadata, contents)
        xml_transcript = xml_builder.build_xml_transcript()





        






main()












