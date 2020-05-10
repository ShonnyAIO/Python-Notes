# Escritura de archivos y dema detalles acerca de manejor de archivos

#Se coloca "w" como segundo argumento del a funcion open() cuando se quiere abrir el archivo en modo lectura.
# El archivo ya debe existir. "w+" si el archivo en cuestión aún no exista, de esta manera lo crea y además lo abre en modo de lectura
"""
#a = open("archivo2.txt", "w+")

#a.write("Hola Johnny \n")

#a.close()
"""

#write() es la que sirve para escribir los archivos, recibe como argumento un string que colocara en el archivo en el cursor actual de escritura



"""
a = open("archivo2.txt", "a")
a.write("Las primeras 7 lineas del abecedario son: \n")

for b in "abcdefg":
	a.write(b +"\n")
	"""



"""
"a" se coloca como segundo argumento de la función open() cuando se quiere abrir el archivo en modo de escritura
sin que se borre el contenido ya escrito en el. Se podrá escribir en el archivo luego de la última línea escrita en el mismo

seek(0) sirve para colocar el cursor de lectura del archivo al principio del mismo
"""

a = open("archivo2.txt", "r")
print(a.read()) 
a.seek(0)
print(a.read())
a.close()

