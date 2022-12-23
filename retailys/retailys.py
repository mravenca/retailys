from io import BytesIO
from zipfile import ZipFile
import urllib.request
from lxml import etree
from datetime import datetime
import os

with urllib.request.urlopen("https://www.retailys.cz/wp-content/uploads/astra_export_xml.zip") as response:
    xmlstr = response.read()
    
    

lines=""

now = datetime.now()
currentTime = now.strftime("%H:%M:%S")
print(currentTime, ": Stahuji a rozbaluji archiv..")
with ZipFile(BytesIO(xmlstr)) as my_zip_file:
    content = my_zip_file.open('export_full.xml').read()
    
now = datetime.now()
currentTime = now.strftime("%H:%M:%S")
print(currentTime, ": Archiv stažen a rozbalen.")
print("Parsuji xml..")

root = etree.fromstring(content)

now = datetime.now()
currentTime = now.strftime("%H:%M:%S")
print(currentTime, ": XML rozparsováno.")
#print("root tag:", root.tag)

items = root.xpath("//export_full/items/item")

for item in items:
     
     parts = item.find('parts')
          
     if parts:
        for p in parts:
            p2 = p.find('item')
            print("Položka: ", item.get('name'), "Díl: ", p2.get('name'))

     else:
         print("Položka: ", item.get('name')," - nemá díly")

print("Konec. Počet položek: ", len(items))  