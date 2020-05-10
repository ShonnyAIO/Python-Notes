
# LOS EJEMPLOS EN DONDE PARTICIPA LA FUNCION INPUT preferiblemente comentarlos a menos que se quiera ver su salida
# Recomiendo leer primero este archivo, analizar cada pequeño ejemplo con un cafe


#SECCION 1
# --------- programar en una sola linea -------------



# sintaxis "pro" no es obligatoria, esto es tan solo para comprender mejor como trabaja exactamene la logica de Python
# y ver todo lo que se puede hacer con este lenguaje que este relacionado con tuplas, diccionarios y conjuntos

# crear tupla de 4 elementos cuyo elementos ingrese el usuario en una sola linea
# usar la funcion tuple para crear tuplas de esta manera
tupla1 = tuple((input() for i in range(4)))  # en este caso serian strings
# print(tupla1)

# tupla de numeros enteros del 1 al 10, notar que depende de lo que se
# coloque dentro de la funcion range, y eso lo sabemos manejar
tupla2 = tuple(i for i in range(1, 11))
# print(tupla2)

# recordando del material dado en la pildora de matrices
lista1 = [i for i in range(2, 42)]  # lista con numeros enteros del 2 al 41
# el siguiente parecido al primer ejemplo dado con las tuplas, pero esta vez una lista
lista2 = [input() for i in range(4)]


# este es un diccionario donde la clave es un numero i, y el dato seria i al cuadrado. i estaria en un rango de 1 a 4
dict1 = {i: i**2 for i in range(5)}
# print(dict1)

# este es un diccionario donde el dato es un nombre y la clave es ese mismo nombre al reves
dict2 = {nombre[::-1]: nombre for nombre in ("Monica", "Pedro", "Alfonso")}
# el detalle esta en que si tenemos un string y luego colocamos "[::-1]" se retornara ese mismo string al reves
# notar que "nombre" es una variable iteradora que recorre una tupla,  entonces en cada iteracion es un string
# de esa tupla, recorre la tupla de izquierda a derecha
# print(dict2)

# si nos volvemos mas ambiciosos podemos llegar hacer esto
dict3 = {nombre[::-1]+str(len(nombre)**2.89): nombre for nombre in tuple(
(input("ingresar nombre: ") for i in range(int(input("ingrese la cantidad de contactos: ")))))}
# estoy claro, ni se entiende a simple vista, tal vez programar en una sola linea no sea lo mas ideal siempre, aunque se vea cool
# es una sola linea tambien, solo que la divide en 2 para intentar que se viera mejor
# lo primero que debemos saber es que es un diccionario en donde las claves son monstruosas, y los datos son los nombres
# imaginemos que es un sistema de contactos,  la calve seria asi:
# el nombre del contacto al reves  + str( numero de caracteres del nombre elevado a 2.89)
# como vemos la clave es mas dificil de decifrar
# vemos que el primer ciclo recorre una tupla, que contendra los nombres (por eso se colcoa el input) 
# pero para que el usuario tambien escriba la cantidad de contactos/nombres  notemos que el ultimo for
# tiene un rango que determina el usuario, que seria desde 0 al entero que ingrese menos 1
#print(dict3)


# un ejemplo mas pero con conjuntos,  el resultado seria {"aa", "ba", "ca"}
set1 = {i+"a" for i in {"a", "b", "c"} }


#SECCION 2
#--------- otra forma de recorrer diccionario usando un for -----------

dict4={1:"pera", 2:"patilla", 3:"mango"}
for v,k in dict4.items():
    print(v, k) # v seria un numero    y k una fruta

#SECCION 3
#------------ comprobacion de pertenencia en diccionarios --------------

dict5 = {"fruta": "guanabana", "figura": "cuadrado", "auto":"mazda 6"}

#el operador in nos puede servir pero solo para verificar si cierto dato es una clave del diccionario

# ejemplo: "fruta" in dict5   seria  True           "edad" in dict5    seria False

#por eso es que a la hora de recorrer un ciclo for con una sola variable iteradora,   esa variable recorreria las claves



#------------- Detalles -----------------
#todas estas estructuras excepto las tuplas poseen el metodo clear()  que lo que hace es vaciar la estructura
# la funcion len() puede recivir no solo listas, sino cualquier estructura iterable
# del puede eliminar variables, listas, conjuntos, objetos, diccionarios y tuplas. 


