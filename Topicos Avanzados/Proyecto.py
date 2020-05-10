"""
n = int(input())
resultados = []
#841, 1!, 5!, 6!

factoriales = (1, 2, 6, 24, 120, 720, 5040, 40320)

for i in factoriales:
	if(n-i >= 0):
		resultados.append(factoriales.index(i))
		n = n-i
	else:
		continue

print(resultados)
"""

factoriales = (1, 2, 6, 24, 120, 720, 5040, 40320)
suma = 0
solucion = False 

resultados = []
num = int(input("Ingrese el numero positivo: "))


for i in range(len(factoriales)):
	resultados.append([])

for i in range(len(factoriales)):
	resultados[0].append(factoriales[i])
	for j in range(i+1, len(factoriales)):
		resultados[1].append(factoriales[i]+factoriales[j])
		for k in range(j+1, len(factoriales)):
			resultados[2].append(factoriales[i]+factoriales[j]+factoriales[k])
			suma = factoriales[0] + factoriales[1] + factoriales[2]
			if(suma == num):
				print("Solucion encontrada :"f'{factoriales[i]}, {factoriales[j]}, {factoriales[k]}')
				suma = 0
				solucion = True
			for l in range(k+1, len(factoriales)):
				resultados[3].append(factoriales[i]+factoriales[j]+factoriales[k]+factoriales[l])
				for m in range(l+1, len(factoriales)):
					resultados[4].append(factoriales[i]+factoriales[j]+factoriales[k]+factoriales[l]+factoriales[m])
if (solucion == False):
	print("No se encontro solucion")
