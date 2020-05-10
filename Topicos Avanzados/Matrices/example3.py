# Es recomendable haber analizado primero el example2.py
# Este programa es un juego de un laberinto
# trabaja con el archivo de texto  llamado "mapa.txt" (debe estar en el mismo directorio que este código)
# En ese archivo se puede editar el laberinto, decidir las dimensiones del mismo, paredes y pasillos
# los sitios vacios con guion bajo "_" las paredes con  numeral "#"
# "L" es la salida , al llegar ese sitio se gana
# Nuestro personaje es un asterisco, que se puede mover tal como en el anterior ejemplo

def mover(x, dir, f, c): # permite mover el personaje y verifica si se ha ganado
    global ganar
    for i in range(c):
        for j in range(c):
            if(x[i][j] == personaje):
 
                if( dir =='d' and not j== c-1):
                    if(not x[i][j+1] == 'x'):
                        if( x[i][j+1] == 'L'): ganar = True
                        x[i][j]=' '; x[i][j+1] = personaje 

                elif(dir == 's' and not i== f-1):
                    if(not x[i+1][j] == 'x'):
                        if( x[i+1][j] == 'L'): ganar = True
                        x[i][j]=' '; x[i+1][j] = personaje

                elif(dir == 'a' and not j==0):
                    if(not x[i][j-1] == 'x'):
                        if( x[i][j-1] == 'L'): ganar = True
                        x[i][j]=' '; x[i][j-1] = personaje

                elif(dir == 'w' and not i==0):
                    if(not x[i-1][j] == 'x'):
                        if( x[i-1][j] == 'L'): ganar = True
                        x[i][j]=' '; x[i-1][j] = personaje
                return

def mostrar_matriz(x):
    for i in x:         
        for j in i:     
            print(j+' |', end=' ')
        print('')



mapa = []    # matriz con la cual se mostrara el laberinto
ganar = False # variable booleana que sirve para verificar si se ha ganado el juego
personaje = '*' 
filas = 0  
columnas = 0  


a = open("mapa.txt", "r")

filas = int(a.readline()) ; columnas = int(a.readline())

for i in range(filas):
    #aux, en cada iteracion es la linea actual, sin el salto de linea
    aux = list(a.readline().strip("\n"))   # recordar que strip  le "le quita" al strung el/los caracteres deseados
    for i in range(len(aux)):
        if(aux[i]=='_'): aux[i]=' '
    # ahora se sustituye en la matriz 
    mapa.append(aux)

mapa[0][0] = personaje


# algoritmo principal del programa

from os import system
while(True):
    system("cls")
    mostrar_matriz(mapa)
    if(ganar):
        print("Has llegado a la meta"); break
    direccion = input()
    mover(mapa, direccion, filas, columnas)