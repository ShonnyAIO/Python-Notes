from random import randint, uniform
from time import time

# vamos a comparar la rapidez de 3 algoritmos de ordenamiento
# el que esta implementado internamente en Python 3 se llama tim sort
# que se aplica cuando usamos el metodo sort() en las listas
# El tradicional pero lento bubblesort
# y por ultimo quick sort
# Se ordenaran en cada caso los elementos de menor a mayor
# En cada caso se llena una lista con 10 mil enteros desordenados (generados de forma aleatorea)

# --------------------- Tim sort -----------------------------
l = []
for i in range(10000):
    l.append(randint(1, 40000))
print("Tim sort: ")
t1 = time()
l.sort()  # <---- tim sort
t2 = time()
print("%.3f" % (t2-t1), "segundos", "\n", l[0:10], "\n")


# ---------------------- Bubble sort -------------------------

l = []
for i in range(10000):
    l.append(randint(1, 40000))

longitud_lista = len(l)-1
# BUBBLE SORT TOMARA ENTRE 30  A 37 SEGUNDOS ORDENARLOS,  TENER PACIENCIA
t1 = time()
# bubble sort
for i in range(longitud_lista):
    for j in range(longitud_lista-i):
        # si un elemento es mayor que el elemento que le sigue, se produce el intercambio
        if(l[j] > l[j+1]):
            aux = l[j+1]
            l[j+1] = l[j]
            l[j] = aux
t2 = time()
print("Bubble sort: ")
print("%.3f" % (t2-t1), "segundos", "\n", l[0:10], "\n")


# -------------------- Quick Sort ---------------------------


l = []

for i in range(10000):
    l.append(randint(1, 40000))

#funcion quickSort RETORNA la lista ordenada
def quickSort(l):
    if(len(l) < 2): return l

    pivot = l[0] ; left = [] ; equal = [] ; right = []

    for i in l:
        if(i < pivot):
            left.append(i)
        elif(i == pivot):
            equal.append(i)
        else:
            right.append(i)

    if( len(left)<2 and  len(right)<2):
        return left + equal + right
    else:
        return quickSort(left)+equal+quickSort(right)



print("Quick sort: ")
t1 = time()
l = quickSort(l)
t2 = time()
print("%.3f" % (t2-t1), "segundos", "\n", l[0:10], "\n")
