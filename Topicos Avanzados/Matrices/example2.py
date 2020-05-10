# Programa en el cual se muestra una  matriz que simula ser un tablero de 3 x 3
# Un asterisco se situa en la esquina superior izquierda y el usuario puede moverlo en 4 direcciones siempre que pueda
# w para arriba s para abajo d para derecha a para izquierda



tablero = [ ['*', ' ',' '] , [' ',' ',' '] , [' ',' ',' '] ]  # tablero


def mostrar_matriz(x): # funcion para mostrar matriz
    for i in x:         
        for j in i:     
            print(j+' |', end=' ')
        print('')

def mover(x, dir):  # funcion que recibe el tablero y la direccion
    for i in range(3):
        for j in range(3):
            if(x[i][j] == '*' ):
                if( dir =='d' and not j==2):
                    x[i][j]=' '; x[i][j+1] = '*' 
                elif(dir == 's' and not i==2):
                    x[i][j]=' '; x[i+1][j] = '*' 
                elif(dir == 'a' and not j==0):
                    x[i][j]=' '; x[i][j-1] = '*' 
                elif(dir == 'w' and not i==0):
                    x[i][j]=' '; x[i-1][j] = '*' 
                return


# algoritmo principal del programa 

from os import system
while(True):
    system("cls")
    mostrar_matriz(tablero)
    x = input()
    mover(tablero, x)