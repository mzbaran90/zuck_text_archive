import os
import re

os.chdir('/Users/MasonBaran/Desktop')

##creates list of lines as to iterate through to fine participants names
line_list = []
i = 0
with open('2018-028.txt','r', encoding='utf-8') as inFile:
    for line in inFile.readlines():
        i += 1
        if line.isspace():
            i -= 1

        if not line.isspace():
            line_list.append(line.strip())
            if line.__contains__('##content##'):
                pos = i



line_list = line_list[pos:] ##cuts everything from ##contents## back


##reads 'line' from line list and compiles a set of names of participants
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



splitStr = '((split))'
contents_with_splitStr = ""
for line in line_list:
    new_line = line
    for name in names:
        if name in line:
            new_line = line.replace(name, splitStr)
    contents_with_splitStr += new_line


split_contents = contents_with_splitStr.split(splitStr)

print(split_contents[1])
stopper = 0
i = 0
index = 1

for participant in list_of_participants:
    if i > stopper:
        stopper += 1
    for line in split_contents[index]:

        if i > stopper:
            break
        elif i == stopper:
            for key, value in participant.items():
                print(key + ':' + split_contents[index] + '\n')
                participant[key] = split_contents[index]
                index += 1
                i += 1
                break



print(list_of_participants)





