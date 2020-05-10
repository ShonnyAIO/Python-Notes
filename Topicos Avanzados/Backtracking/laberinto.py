from os import system

# Programa que utilizando la tecnica de backtracking
# encuentra la salida de un laberinto

# En el mismo directorio que este programa debe estar
# un archivo .txt  llamado lab en el que este escrito el laberinto
# se denota con "P" al personaje  Y "S" la salida
# con "#" para las paredes  y "." los espacios libres

archivo = open("lab.txt", "r")


# se crea la matriz que simulara el mapa
mapa = []
for lines in archivo:
    mapa.append(list(lines.strip("\n")))
archivo.close()

# funcion que imprime el mapa


def mostrar_mapa():
    for i in mapa:
        for j in i:
            print(j, end=" ")
        print(" ")


personaje = "P"
filas = len(mapa)
columnas = len(mapa[0])

# se busca la posicion del personaje
pos_i = pos_j = 0
for i in range(filas):
    for j in range(columnas):
        if("P" == mapa[i][j]):
            pos_i = i
            pos_j = j
            break
# se busca la posicion de la salida
pos_salida1 = pos_salida2 = 0
for i in range(filas):
    for j in range(columnas):
        if("S" == mapa[i][j]):
            pos_salida1 = i
            pos_salida2 = j
            break

# la siguiente funcion verifica si es posible moverse a la posicion i j
# el primer condicional verifica si se esta intentando salir del tablero
# el 2do ve si la casilla a donde se intenta mover hay una pared o ya fue recorrida


def verificar_direccion(i, j):
    if(i < 0 or j == columnas or i == filas or j < 0):
        return False
    if(mapa[i][j] == "#" or mapa[i][j] == "*"):

        return False
    return True

# verifica si ya se "piso" la casilla donde estaba la "S" que indica la salida
# se retorna el booleano que resulta de la siguiente expresion logica


def salida_encontrada():
    return mapa[pos_salida1][pos_salida2] == "P"


def busqueda_salida(i, j, mapa):

    system("cls")
    mostrar_mapa()
    input("Presione una tecla para continuar al siguiente estado")

    # se verifica si se encontro la salida
    if(salida_encontrada()):
        system("cls")
        print("Solucion encontrada")
        mostrar_mapa()
        input("Presione una tecla para terminar")
        return True

    # se verifica si es posible moverse direccion este
    if(verificar_direccion(i, j+1)):

        mapa[i][j] = "*"
        j += 1
        aux = mapa[i][j]
        mapa[i][j] = personaje
        if(not busqueda_salida(i, j, mapa)):
            mapa[i][j] = aux
            j -= 1
            mapa[i][j] = personaje
        else:
            return True

    # se verifica si es posible moverse direccion sur
    if(verificar_direccion(i+1, j)):

        mapa[i][j] = "*"
        i += 1
        aux = mapa[i][j]
        mapa[i][j] = personaje
        if(not busqueda_salida(i, j, mapa)):
            mapa[i][j] = aux
            i -= 1
            mapa[i][j] = personaje
        else:
            return True

    # se verifica si es posible moverse direccion oeste
    if(verificar_direccion(i, j-1)):

        mapa[i][j] = "*"
        j -= 1
        aux = mapa[i][j]
        mapa[i][j] = personaje
        if(not busqueda_salida(i, j, mapa)):
            mapa[i][j] = aux
            j += 1
            mapa[i][j] = personaje
        else:
            return True

    # se verifica si es posible moverse direccion norte
    if(verificar_direccion(i-1, j)):

        mapa[i][j] = "*"
        i -= 1
        aux = mapa[i][j]
        mapa[i][j] = personaje
        if(not busqueda_salida(i, j, mapa)):
            mapa[i][j] = aux
            i += 1
            mapa[i][j] = personaje
        else:
            return True
    # si se llega hasta aqui es poque el personaje esta atascado, se cometio antes una mala desicion
    # se retorna falso para matar el ambiente actual y regresar al anterior y probar otro arbol de posibilidades
    return False


# se invoca la funcion del backtracking
busqueda_salida(pos_i, pos_j, mapa)
