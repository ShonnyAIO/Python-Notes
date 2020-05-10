# Si queremos buscar un elemento en alguna estructura de datos
# podemos usar el operador in que hemos visto antes

x = 2 in [1,2,3] # x almacenaria verdadero, pues 2 estaria en la lista

# pero en otros lenguajes esto no seria tan sencillo, tendriamos que recorrer la estructura
# con un ciclo y mediante comparaciones verificar si esta o no el elemento
# hacer un recorrido lineal no es el algoritmo mas eficinete, en seguida se expone
# el famoso algoritmo llamado busqueda binaria. 
# La condicion para aplicar este algoritmo es que la estructura de datos este ordenada



def busqueda_binaria( lista, elemento_a_buscar):

    indice_inferior=0
    indice_superior=len(lista)-1

    while(indice_inferior < indice_superior):

        indice_medio = (indice_inferior+indice_superior)//2
        # aprovecho para decir que en Python 3 "is" es analogo al operador de indentidad logica "=="
        if elemento_a_buscar is lista[indice_medio]:
            return indice_medio
        elif elemento_a_buscar > lista[indice_medio]:
            indice_inferior = indice_medio+1
        else:
            indice_superior = indice_medio-1
    # si el elemento no fue encontrado se retorna -1
    return -1

l=[1,19,32,78,102,325, 401,811, 9801]

#buscaremos el 19 en la lista l,  la variable a almacenará el indice del elemento
a=busqueda_binaria(l, 19)
print(a)