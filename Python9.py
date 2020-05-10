
"""
a = [1, 20, 30, "Jonathan", "Google"]

print(a)
print(a[0])

for i in a:
	print(i, end=' ')

a.append(5)
a.append(input("Ingrese una palabra: "))
print(a)
a.pop()
print(a)


#append(): Es una funcion que sirbe para añadir un elemento a la lista.
#pop(): Sirve para eliminar el último elemento ingresado en la lista.
#len(): Cantidad de posiciones en la lista
"""

l = [1,0,1,43.12,0,1,0,True,1]
k = 0
j = 0
for i in range(7):
	if(l[i] == 1): k+=1
	if(l[i] == 0): j+=1

if(k>=j):
	print(k)