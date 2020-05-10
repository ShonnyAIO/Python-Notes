def mostrar_matriz(x):
	for i in x:
		for j in i:
			print(str(j) + ' | ', end = ' ')
		print(' ')

l = [[1.1, True, 4], [2.1, 'abc4', 9]]
mostrar_matriz(l)

print(l[0][0])
print(l[1][2])

p = []

for i in range(2):
	aux = []
	for i in range(2):
		aux.append(int(input()))
	p.append(aux)

mostrar_matriz(p)