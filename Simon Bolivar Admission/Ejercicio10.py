# OPCION B, Ejercicio 36
def par(n):
    return n%2 == 0

def comprobar(ecuacion):
    if(par(ecuacion)):
        print("Siempre es par")
    else:
        print("Siempre es impar")

pares = [2,4,6,8,10,12]
impares = [1,3,5,7,9,11]
ecuacion = 0
for i in pares:
    for j in impares:
        ecuacion = i + j
        comprobar(ecuacion)

