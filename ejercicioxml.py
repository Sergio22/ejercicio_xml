# -*- encoding: UTF-8 -*-
from xml.dom import minidom
xmldoc = minidom.parse("proyecto.xml")
itemlist = xmldoc.getElementsByTagName("address_component")
for items in itemlist:
	tipo = items.getElementsByTagName("type")[0].firstChild.data
	if tipo=="administrative_area_level_2":
		print ("Provincia:")
		print items.getElementsByTagName("long_name")[0].firstChild.data