a = 5; b = "casa" ; c = 1234.456
print("A =",a, "B =",b, "C =",c)
print("A = {0} B = {1} C = {2}".format(a,b,c))
print(f"A = {a} B = {b} C = {c}")
h = f"A = {a} B = {b} C = {c}"
print(h)

# %d -> Entero ; %s -> String ; %f -> Flotantes

print("A = %d B = %s C = %f" % (a,b,c))
print("A = %d B = %s C = %.3f" % (a,b,c))

# Modulos -> Funciones que incluye en el lenguaje

import math
a = math.log2(64) ; print("A = %d" % a)
b = math.sqrt(625) ; print("B = %d" % b)


import random

a = random.randint(1,100) ; print(a)
b = random.uniform(1,100) ; print(b)

from math import sin, fabs, radians

a = fabs(5-7) ; print(int(a), end=' ') #end lo pones en la misma línea
b = sin(radians(45)) ; print(b)