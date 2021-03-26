# Ejercicio 29, Opcion C
a = 9
b = (a**2 - a)
c = (3*a - 3)
d = (2*a - 1)
e = (a**3 - 1)
f = (a + 3**a)
x = 1
ecuaciones = [b,c,d,e,f]
for i in ecuaciones:
    if(i%2 != 0):
        print("Ecuacion N:", x, i)
    x = x+1