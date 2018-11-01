import xml.etree.ElementTree as ET
from xml.dom import minidom


class xml_builder(object):

    def __init__(self, metadata, contents):
        self.metadata = metadata
        self.contents = contents

    def build_xml_transcript(self):

        root = ET.Element('transcript')
        for key, value in self.metadata.items():
            key = ET.SubElement(root, key)
            key.text = value

        for participant in self.contents:
            for key, value in participant.items():
                speaker = ET.SubElement(root, 'participant', attrib={'name': key})
                speaker.text = value

        xml_formatted = self.prettyprint(root)
        print(xml_formatted)
        return xml_formatted

    def prettyprint(self, root):
        #helper method to print formatted xml document

        un_formatted = ET.tostring(root, 'utf-8')
        re_parse = minidom.parseString(un_formatted)
        return re_parse.toprettyxml(indent="    ")

