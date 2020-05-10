contador_soluciones = 0


def sumar(candidato, numero):
	suma = 0
	for i in candidato:
		suma = suma+i
	return suma == numero


def busqueda(lista, numero, conjunto_candidato, i, j):
	global contador_soluciones

	if(len(candidato) == 3):
		if(sumar(candidato, n)):
			contador_soluciones = contador_soluciones + 1
			print(f"Solucion encontrada: ")
			combinaciones = []
			for i in candidato:
				for j in lista:
					if(i == j):
						combinaciones.append(lista.index(j)+1)

			#for i in candidato:
			#	print(i, end="! ")
			combinaciones.sort()
			for i in combinaciones:
				print(i, end="! ")
		else:
			return False
	else:
		while(i < j):
			candidato.add(lista[i])
			if(not busqueda(lista, n, candidato, i+1, j)):
				candidato.remove(lista[i])
				i += 1



n = int(input("Ingrese un numero: "))

lista = (1, 2, 6, 24, 120, 720, 5040, 40320)
candidato = set()
busqueda(lista, n, candidato, 0, 8)
if(contador_soluciones == 0):
	print("No se encontro soluciones")


