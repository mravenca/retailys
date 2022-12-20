from io import BytesIO
from zipfile import ZipFile
import urllib.request
from xml import sax

url = urllib.request.urlopen("https://www.retailys.cz/wp-content/uploads/astra_export_xml.zip")


# define a Custom ContentHandler class that extends ContenHandler
class CustomContentHandler(sax.ContentHandler):
    def __init__(self):
        self.itemCount = 0

    # Handle startElement
    def startElement(self, tagName, attrs):
        global itemCount
        if tagName == 'export_full':
            print('Datum exportu: ' + attrs['date'] + " verze: " + attrs['version'])
        elif tagName == 'items':
            pass        
        elif tagName == 'item':
            print('Název: ' + attrs['name'])
            self.itemCount += 1
    
    # Handle endElement
    def endElement(self, tagName):
        if tagName == 'item':
            pass

    # Handle startDocument
    def startDocument(self):
        print('Začátek')

    # Handle endDocument
    def endDocument(self):
        print('Konec')
        print('Počet položek: ', self.itemCount)

lines=""

with ZipFile(BytesIO(url.read())) as my_zip_file:
    for contained_file in my_zip_file.namelist():
        content = my_zip_file.open(contained_file).readlines()
        #-------------------------------------------------------------
        for line in content:
            ld = line.decode("utf-8")
            lines += ld
            #print(ld)
        #--------------------------------------------------------------

sax.parseString(lines, CustomContentHandler())
