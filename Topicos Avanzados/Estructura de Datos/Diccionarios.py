# ------- Diccionarios ------------


dic0 = {'manuel' : 4098, 'barbara' : 9139}


dic1 = {True: 2, 5.1: [1,3,9], 1: {2,3}}

dic0['alex'] = 2127
print(dic0)



del dic0['barbara']
print(dic0)

dic2 = {1: "impar", 2: "par", 3: "impar"}

for i in dic2:
	#print(i, end=" ") Acceder al indice
	print(dic2[i], end=" ") #Acceder a la variable

