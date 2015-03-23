# -*- encoding: UTF-8 -*-
from xml.dom import minidom
xmldoc = minidom.parse("proyecto.xml")
itemlist = xmldoc.getElementsByTagName("address_component")

print("Ubicacion: ")
print itemlist[0].getElementsByTagName("long_name")[0].firstChild.data
opcion =1
while opcion!=0:

	print ("Elige una opcion:")
	print ("1.- Codigo postal")
	print ("2.- Provincia")
	print ("3.- Comunidad Autónoma")
	print ("4.- País")
	print ("5.- Latitud y longitud")
	print ("0.- Salir")
	opcion=int (input("Elige una opcion:"))

	if opcion == 1:
		variable = "postal_code"
		print ("Código Postal:")
	if opcion == 2:
		variable = "administrative_area_level_2"
		print ("Provincia:")
	if opcion == 3:
		variable = "administrative_area_level_1"
		print ("Comunidad Autónoma:")
	if opcion == 4:
		variable = "country"
		print ("País:")
		
		
	for items in itemlist:
		tipo = items.getElementsByTagName("type")[0].firstChild.data
		if tipo == variable:
			print items.getElementsByTagName("long_name")[0].firstChild.data
			break
		
	if opcion == 5:
		pos = xmldoc.getElementsByTagName("location")
		print "Latitud"
		
		print pos[0].getElementsByTagName("lat")[0].firstChild.data
		print "longitud"
		print pos[0].getElementsByTagName("lng")[0].firstChild.data