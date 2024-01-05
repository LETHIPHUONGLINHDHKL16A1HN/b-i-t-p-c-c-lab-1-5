import xml.etree.ElementTree as ET
class XMLReader:
    def __init__(self, file_path):
        self.file_path= file_path
        self.data= None
    def reader_xml(self):
        tree=ET.parse(self.file_path)
        self.data=tree.getroot()
    def display_data(self):
        if self.data:
            for product in self.data 