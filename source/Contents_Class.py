import os
import re



class Contents():


    def __init__(self, file):
        self.file = file + '.txt'



    def open_file_create_reader_object_instance(self, file):
        with open(file, 'r', encoding='utf-8')as infile:
            reader = infile.read()
            return reader

    def get_contents_index(self):

        reader = self.open_file_create_reader_object_instance()
        content_pos = reader.find('##content##') + "##content##".__len__()

        return reader[content_pos:]

    def isolate_utterances(self,contents):

        regex = re.compile(r'^##.+?##', flags=re.DOTALL and re.MULTILINE)
        names = regex.findall(contents)
        utterances = re.split(regex, contents)
        return names, utterances

    def content_creator(self):
        self.reader = self.open_file_create_reader_object_instance(self.file)
        self.contents = self.get_contents_index()
        self.seperate_utterances = self.isolate_utterances(self.contents)











