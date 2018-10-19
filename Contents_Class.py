import os
import re

os.chdir('/Users/MasonBaran/Desktop/zuck_txt_testing')

class Contents(object):


    def __init__(self, file):
        self.file = file + '.txt'





#creates list of lines (line_list) from single file input as to iterate through to fine participants names.
#Blank lines are not appended to this list. Index is decremented by 1 if a blank line is encounter. After file has
#been iterated, the pos is assigned the index value. Position is then passed to sub string line_list.'''

    def seperate_contents(self):


        line_list = []
        index = 0

        with open(self.file,'r', encoding='utf-8') as inFile:
            for line in inFile.readlines():
                index += 1
                if line.isspace():
                    index -= 1

                if not line.isspace():
                    line_list.append(line)
                    if line.__contains__('##content##'):
                        pos = index


            return line_list[pos:]      #line_list is now comprised of everything ##contents## on




#reads 'line' from line list and compiles a set of names of participants using a regular expression. A set and dictionary
#are created. The set is made to save memory when searching lines for list of names. Each dictionary represents a
#participant. Before name is added to dictionary hash tags are removed. After name is found participant is appended to
#list_of_participants
#       Sets name compiler and participant creator
    def participant_creator(self, line_list):
        names = set()
        regex = re.compile(r'##.+##')
        list_of_participants = []
        for line in line_list:
            for result in re.findall(regex, line):
                participant = {}
                names.add(result)
                if '##' in result:
                    resultStr = result
                    no_hash = resultStr.replace('##', '')

                    participant[no_hash] = ""
                list_of_participants.append(participant)

        return names, list_of_participants


#iterates through line_list and replaces all isntances of names with splitStr. Each line is appended
#to contents_with_splitStr. After iterator finished, contents_with_splitStr are now split ---> split_contents'''
#       splitStr_adder
    def split_string_adder(self,line_list, names):
        splitStr = '((split))'
        contents_with_splitStr = ""
        for line in line_list:
            new_line = line
            for name in names:
                if name in line:
                    new_line = line.replace(name, splitStr)     #instances of names are now replaced with splitStr
            contents_with_splitStr += new_line


        split_contents = contents_with_splitStr.split(splitStr)     #new array of contents split on splitStr
        return split_contents



#The following assigns one array entry to a value in the list_of participants. Ex. the first dictionary or participant
#in the list of dictionaries or participants will recieve the text that followed the participant as its value. Note the index
#of the split_contents being assigned starts at 1. This is because the first split_contents value will be ''. The variables i
#and stopper are checked against each other to ensure only one entry from split_contents is assigned to a participant'''
#       value assigner
    def value_assign(self,list_of_participants, split_contents):
        stopper = 0     # stopper variable created to be compared against i
        i = 0           # to be compared against stopper
        index = 1       # keeps track of index of split_contents values

        for participant in list_of_participants:
            if i > stopper:
                stopper += 1
            for line in split_contents[index]:

                if i > stopper:
                    break
                elif i == stopper:
                    for key, value in participant.items():
                        participant[key] = split_contents[index]
                        index += 1
                        i += 1
                        break

        return list_of_participants

    def content_creator(self):
        line_list = self.seperate_contents()
        names, list_of_participants = self.participant_creator(line_list)
        split_contents = self.split_string_adder(line_list, names)
        self.participant_values = self.value_assign(list_of_participants, split_contents)
        return self.participant_values











