from os import system


# Se crea la matriz de 9 x 9 donde se pondran los numeros del sudoku
l = [[0 for i in range(9)] for i in range(9)]
contador_soluciones = 0


def mostrar_matriz(x):  # funcion para mostrar la matriz con "casillas"
    for i in x:
        for j in i:
            print(str(j)+' | ', end=' ')
        print('')

# funcion que verifica si el sudoku esta listo
def sudoku_listo(l):

    #verifica si la suma de los numeros de cada fila da 45, en caso contrario se retorna falso
    suma = 0
    for i in l:
        for j in i:
            suma += j
        if(not suma == 45):
            return False
        suma = 0
    #verifica si la suma de los numeros de cada columna  da 45, en caso contrario retorna falso
    for i in range(9):
        for j in range(9):
            suma += l[j][i]
        if(not suma == 45):
            return False
        suma = 0

    #verifica si la suma de los numeros que estan en la diagonal que va desde la esquina
    # superior izquierda hasta la esquina inferior derecha
    # da 45, en caso contrario retorna falso
    suma = 0
    i = j = 0
    while(i < 9 and j < 9):
        suma += l[i][j]
        i += 1
        j += 1
    if(not suma == 45):
        return False

    #verifica si la suma de los numeros que estan en la diagonal  que va desde la esquina
    #inferior izquierda hasta la esquina superior derecha
    # da 45, en caso contrario retorna falso
    suma = 0
    i = 8
    j = 0
    while(i > -1 and j < 9):
        suma += l[i][j]
        i -= 1
        j += 1
    if(not suma == 45):
        return False

    return True

# Verfica si hay un numero repetido en una de las 9 submatrices del sudoku
# es invocada por la funcion es_valido()
def verificar_repetidos_submatriz(l, filas, columnas):
    lista_submatriz = []
    for i in filas:
        for j in columnas:
            lista_submatriz.append(l[i][j])
    # si no hay 0s en la submatriz, no hay nada que verificar, ya anteriormente se verifico
    if(0 in lista_submatriz):
        lista_submatriz.sort()
        for i in range(0, 8):
            if(not lista_submatriz[i] == 0 and lista_submatriz[i] == lista_submatriz[i+1]):
                return False
    return True

# verifica si es prundente colocar el numero candidato en la casilla  i j
def es_valido(l, i, j, numero_candidato):
    aux = j
    aux2 = i
    j = 0
    while(j < 9):
        if(l[i][j] == numero_candidato):
            return False
        j += 1
    i = 0
    while(i < 9):
        if(l[i][aux] == numero_candidato):
            return False
        i += 1

    if(aux == aux2):
        i = j = 0
        while(i < 9 and j < 9):
            if(l[i][j] == numero_candidato):
                return False
            i += 1
            j += 1

    if(aux+aux2 == 8):
        i = 8
        j = 0

        while(i > -1 and j < 9):
            if(l[i][j] == numero_candidato):
                return False
            i -= 1
            j += 1

    for i in [range(3), range(3, 6), range(6, 9)]:
        for j in [range(3), range(3, 6), range(6, 9)]:
            # de esta manera se verifica si hay numeros repetidos
            # en cada submatriz del sudoku
            bool1 = verificar_repetidos_submatriz(l, i, j)
            if(not bool1):
                return False

    return True

# Esta es la funcion que hace backtracking
def hacer_sudoku(l, i, j, numeros_colocados):
    global contador_soluciones

    # Si se colocaron 81 (9x9) numeros, se debio resolver el problema
    if(numeros_colocados == 81):
        if(sudoku_listo(l)):
            contador_soluciones += 1
            system("clear")
            print(f"Solucion encontrada #{contador_soluciones}")
            mostrar_matriz(l)
            input("Ingrese una tecla para continuar")
            return False

    
    # las siguientes 3 instrucciones son para mostrar los pasos del backtracking
    '''
    system("cls")
    mostrar_matriz(l)
    input("Ingrese una tecla para continuar")
    '''

    numero_candidato = 0
    while(i < 9):
        while(j < 9):
            numero_candidato += 1
            
            if(numero_candidato > 9):
                # se retorna falso porque si se probo todos los numeros del 1 al 9
                # y aun estamos tanteando en la misma casilla, por tanto, se debio cometer un error
                # anteriormente
                return False
            if(es_valido(l, i, j, numero_candidato)):
                l[i][j] = numero_candidato
                numeros_colocados += 1
                j += 1
                if(j > 8):
                    i += 1
                    j = 0
                if(not hacer_sudoku(l, i, j, numeros_colocados)):
                    # si regresamos a este ambiente, colocamos 0 en la actual casilla
                    # y se intenta con otro numero candidato
                    j -= 1
                    if(j == -1):
                        i -= 1
                        j = 8
                    l[i][j] = 0
                    numeros_colocados -= 1



# argumentos:  matriz, indice i=0, indice j=0 y cantidad de numeros colocados
hacer_sudoku(l, 0, 0, 0)

input("Programa finalizado, presiente una tecla para terminar")