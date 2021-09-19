import math

def tamanoPaso(a, b, n):
    list = []
    for i in range(a, n+1):
        x = i*b
        print("x",i," ",x)
        list.append(x)
    return list


def puntoMedio(lista, a, n):
    results = []
    i = 0
    while(i <= n+1):
        if(i+1 == 13):
            break
        xt = (lista[i] + lista[i+1])/2
        print("x",i+1," ", xt)
        results.append(xt)
        i = i+1
    return results

def calcular(lista):
    y = 0
    for i in lista:
        a = 2/i+1
        print("x",y+1,"",a)
        y = y+1


a = 1; b = 0.24; n = 12

print("Tamaño del paso")
h = tamanoPaso(a,b,n)

print("")
print("")
"""
print("Punto medio")
resultados = puntoMedio(h, a, n)

print("")
print("")

"""
calcular(h)

 