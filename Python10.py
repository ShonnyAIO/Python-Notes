archivo = open("archivo1.txt","r")
#r : Modo de lectura
#w : Modo de escritura

for linea in archivo:
	if(linea == 'i\n' or linea == 'e\n') : continue
	print(linea)


print(archivo.read())
archivo.close()


