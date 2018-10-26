import re



class Contents():

    def __init__(self, file):
        self.file = file + '.txt'


    def open_file_create_reader_object_instance(self):
        with open(self.file, 'r', encoding='utf-8')as infile:
            reader = infile.read()
            return reader

    def get_contents_index(self, reader):

        reader = self.open_file_create_reader_object_instance()
        content_pos = reader.find('##content##') + "##content##".__len__()

        return reader[content_pos:]

    def isolate_utterances(self,contents):

        regex = re.compile(r'^##.+?##', flags=re.DOTALL and re.MULTILINE)
        names = regex.findall(contents) #list of names with hashtag symbols

#iterate through list and replaces index with no hashtag name
        for index, name in enumerate(names):
            names[index] = re.sub('[##]*','', name)

        utterances = re.split(regex, contents)

        return names, utterances

    def assign_key_and_value(self, names, utterances):
        pass

    def content_creator(self):
        reader = self.open_file_create_reader_object_instance()
        contents = self.get_contents_index(reader)
        sep_names, sep_utterances = self.isolate_utterances(contents)
        list_of_participant_values = self.assign_key_and_value(sep_names, sep_utterances)
        self.isolate_utterances(contents)












