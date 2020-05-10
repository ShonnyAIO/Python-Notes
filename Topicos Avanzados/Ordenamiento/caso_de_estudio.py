from random import randint, uniform
from time import time

# vamos a ordenar una lista que contengan objetos de la siguiente clase
# luego veremos que no podemos usar el metodo sort para lograr este objetivo de forma directa
# Sera una lista "l" con 10 objetos de esa clase
# queremos que el primer elemento sea el objeto con el menor entero y el menor flotante
# y que el ultimo elemento sea con el mayor entero y mayor flotante


class A:
    def __init__(self, a, b):
        self.__flotante = a
        self.__entero = b

    def return_int(self):
        return self.__entero

    def return_float(self):
        return self.__flotante

    def asignar_int(self, a):
        self.__entero = a

    def asignar_float(self, a):
        self.__flotante = a


l = []

for i in range(10):
    objeto = A(uniform(1, 10000), randint(1, 10000))
    # se trata de crear una lista llena de objetos, con atributos numericos
    l.append(objeto)
    # queremos usar un algoritmo de ordenamiento para ordenar de menor a mayor los numeros
    # mostraremos en pantalla de menor a mayor los enteros y luego del mismo modo los flotantes
    # notar que no podemos usar el metodo sort en este caso para lograr nuestro objetivo

# recordar hay 10 elemtos,  entonces los indices de la lista que recorreremos sera del 0 al 9

# aplicamos un bubble sort  modificado de acuerdo a lo que se tiene que hacer

print("\nRealizando ordenamiento con bubble sort: ")
longitud_lista = len(l)-1
for i in range(longitud_lista):
    for j in range(longitud_lista-i):
        # realizar comparacion para el enteros del objeto(j) con el del siguiente objeto(j+1)
        if(l[j].return_int() > l[j+1].return_int()):
            aux = l[j+1].return_int()
            l[j+1].asignar_int(l[j].return_int())
            l[j].asignar_int(aux)
        # realizar comparacion para el flotante del objeto(j) con el del siguiente objeto(j+1)
        if(l[j].return_float() > l[j+1].return_float()):
            aux = l[j+1].return_float()
            l[j+1].asignar_float(l[j].return_float())
            l[j].asignar_float(aux)

print("\nEnteros ordenados")
for i in range(10):
    print(l[i].return_int(), end=' ')

print("\n\nFlotantes ordenados")
for i in range(10):
    print("%.3f" % l[i].return_float(), end=' ')


# Notar que a los algoritmos de ordenamientos  vistos se les hizo modificaciones
# para poder actuar en este caso en donde se trabajo con programacion orientada a objetos
l = []

for i in range(10):
    objeto = A(uniform(1, 10000), randint(1, 10000))
    # se trata de crear una lista llena de objetos, con atributos numericos
    l.append(objeto)
# quick sort para ordenar en la lista los atributos enteros de los objetos almacenados en ella


def quickSort_enteros(l):

    if(not (len(l) > 1)):
        return l

    pivot = l[0].return_int()
    left = []
    equal = []
    right = []
    for i in l:
        if(i.return_int() < pivot):
            left.append(i)
        elif(i.return_int() == pivot):
            equal.append(i)
        else:
            right.append(i)

    n = len(left)
    n2 = len(right)

    if((n == 0 or n == 1) and (n2 == 0 or n2 == 1)):
        return left + equal + right
    else:
        return quickSort_enteros(left)+equal+quickSort_enteros(right)

# funcion con el mismo algoritmo pero los respectivos flotantes de los objetos


def quickSort_flotantes(l):

    if(not (len(l) > 1)):
        return l

    pivot = l[0].return_float()
    left = []
    equal = []
    right = []
    for i in l:
        if(i.return_float() < pivot):
            left.append(i)
        elif(i.return_float() == pivot):
            equal.append(i)
        else:
            right.append(i)

    n = len(left)
    n2 = len(right)

    if((n == 0 or n == 1) and (n2 == 0 or n2 == 1)):
        return left + equal + right
    else:
        return quickSort_flotantes(left)+equal+quickSort_flotantes(right)


print("\n\nRealizando ordenamiento con Quick sort: ")

l = quickSort_enteros(l)
print("\nEnteros ordenados")
for i in range(10):
    print(l[i].return_int(), end=' ')

l = quickSort_flotantes(l)
print("\n\nFlotantes ordenados")
for i in range(10):
    print("%.3f" % l[i].return_float(), end=' ')
