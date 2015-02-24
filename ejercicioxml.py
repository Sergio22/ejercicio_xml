# -*- encoding: UTF-8 -*-
from xml.dom import minidom
xmldoc = minidom.parse("proyecto.xml")
itemlist = xmldoc.getElementsByTagName("titulo")
print (len (itemlist))