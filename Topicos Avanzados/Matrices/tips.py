

def mostrar_matriz(x):

    for i in x:        
        for j in i:     
            print(str(j)+' |', end=' ')
        print('')



# ejemplo de otro metodo para crear una matriz (en este ejemplo es de 2 x 3)

'''
matriz = []
for i in range(2):
    l = [int(input()) for i in range(3)] ; matriz.append(l)

mostrar_matriz(matriz)
'''

# manera aún más simplificada

#matriz =[[int(input()) for i in range(3)] for i in range(2) ] ; mostrar_matriz(matriz)


#obtener el numero de filas y columnas de una matriz
'''
m=[[1,2,56],[1,3,4]]
filas=len(m); columnas=len(m[0])
'''




# metodo de las listas remove()  (elimina la el elemento que se coloque entre parentesis, en su primera aparicion)


'''
l = [1,3,5,49,3,8]
l.remove(3); print(l)
'''


# ahora veamos el metodo sort(), que es para ordenar los elementos de una lista
# veremos luego fuertes algoritmos para ordenar una cantidad abrumadora de elementos

# ordenar una lista de numeros de forma ascendente

#l=[17.3, 4, 7, 13, 41.1, 1] ; l.sort(); print(l)

# ordenar una lista de numeros de forma descendente

#l=[3, 4.1, 11.7, 91]; l.sort(reverse=True); print(l)

# en este ejemplo, la lista de strings se ordenara alfabeticamente (Aa-zZ)

#l=['a', 'ee', 'ccc', 'dddd', 'b']; l.sort() ; print(l)   # con l.sort(reverse=True) se ordenaria al reves


#ahora se ordenara en base al tamaño de los strings

#l=['abjfhja', 'ajf', 'c', 'afjkaak']; l.sort(key=len, reverse=True); print(l)   

# los argumentos key y reverse en el metodo sort son opcionales, key sirve para cambiar en base a qué se hara el ordenamiento
# en este caso fue en base a la logintud de los strings,  reverse=True es para indicar que se ordenara de mayor a menor


# "ordenando" matrices

#matriz=[[133,3], [4,3], [12, 9]]

#matriz.sort() ; print(matriz) # se vera la matriz ordenada de forma ascendente en base a los primeros elementos de cada "fila"
#matriz.sort(key=lambda x: x[1]) ; print(matriz) # se vera la matriz ordenada de forma ascendente en base a los segundos elementos de cada "fila"

# mas luego veremos las funciones lambda. Se puede aprovechar este ejmplo para empezar una investigacion voluntaria acerca de ellas

# la funcion help() se encarga de imprimir informacion acerca de una funcion de python
# el nombre de la funcion de la cual queremos informacion se debe colocar dentro de los parentesis de help()


# en este ejmplo se nos explicara para que sirve la funcion print
#help(print)

#en este ejemplo, list   tiene mucha informacion, al dar enter podremos ir hacia abajo, si bajamos lo suficiente podremos ver todos los metodos de las listas

#help(list)     

#ejemplo for decreciente, recordar que los for son importarte para recorrer estructuras de datos, como listas, matrices, strings, etc
'''
for i in range(10, 0, -1):
    print(i)
'''