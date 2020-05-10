from time import time


print("Modo recursivo")

def fibo(n):
    if n < 2:
        return n
    return fibo(n-2) + fibo(n-1)

x = int(input("Ingrese un numero positivo n: "))
print("Se imprimira los n primeros terminos de la sucesion de fibnacci: ")

time1=time()
for i in range(x):
    print(fibo(i), end=' ')
time2=time()
print(f"\nTiempo: {time2-time1}")


#-------------------------   AHORA UTILIZANDO UNA ESTRUCTURA DE DATOS PARA
#-------------------------   NO TENER QUE HACER CALCULOS INNECESARIOS

 

print("\nMemorizando")

memoria = {0: 0, 1: 1}

def fibo_mem(n):
  
    if not n in memoria:
        memoria[n]= fibo_mem(n-1) + fibo_mem(n-2)
    return memoria[n]

x = int(input("Ingrese un numero positivo n: "))
print("Se imprimira los n primeros terminos de la sucesion de fibnacci: ")

time1=time()
for i in range(x):
    print(fibo_mem(i), end=' ')
time2=time()

print(f"\n Tiempo: {time2-time1}")

input()
