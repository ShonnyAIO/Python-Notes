from os import system
from math import inf

denominaciones = set()
cantidad = 0


def divisible(a, i):
    for j in a:
        if i/j == 1:
            return True
    return False

def money():
    # lista que nos ayudara a "memorizar"
    lista_men=[inf for i in range(cantidad+1)]
    lista_men[0]=0
   

    for i in range(len(lista_men)):
        if lista_men[i] is inf:
            if divisible(denominaciones, i):
                lista_men[i] = 1; continue

            for j in denominaciones:
                if j > i: break
            
                if lista_men[i] > lista_men[i-j]+1:
                    lista_men[i] = lista_men[i-j]+1
           

    # Se imprime el numero minimo de monedas que se necesitan
    print(lista_men[len(lista_men)-1])



for i in range(int(input("Ingrese la cantidad de denominaciones: "))):
    denominaciones.add(int(input(f"Ingrese la denominacion #{i+1}: ")))

cantidad = int(input("Ingrese la cantidad que se quiere obtener: "))

print(f"La menor cantidad de monedas para obtener {cantidad} es:")
money()

input()