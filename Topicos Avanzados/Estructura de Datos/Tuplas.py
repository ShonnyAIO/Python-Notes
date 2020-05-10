# Tuplas: Estructura de dato que no se puede editar

a = (5, "hola", True)
print(a)
# La ventaja es que no se puede editar
variable = 3
b = (1, variable, "abc")
#print(b[1])
#b[2] = 5, no se pued modificar da error
"""
c = ( int(input()), input(), input() )
print(c)
"""
d = 3, #Una variable
d = (3, ) #Es una tupla

e = (25, "Venezuela", "Jonathan")
# edad, pais, nombre = e
#print(edad, pais, nombre)

#for i in e:
#	print(i)

"""
for i in ( (9, 7.8, "abc", [3, True], input()), (1,2,3) ):
	print(i, end=" ")
"""
a = [1,2,3,5]
mi_tupla = tuple(a); print(mi_tupla)

string = "abc"
print(tuple(string))

g = (1,3,1,6,1,3)
print(g.count(1)) #Cuenta las veces que aparece
print(g.index(3)) #Te indica el indice que aparece el primer elemento

print(g+e) #Union

z = g+e+(9,1,2)
print(z)

v = ("casa", "perro", True); v+=3,

