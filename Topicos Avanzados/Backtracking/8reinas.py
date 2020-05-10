from os import system
from sys import exit


# l es una matriz que hace papel de tablero  (8x8)

l = [[" " for i in range(8)] for i in range(8)]


reina = "R" # reina, nuestras reinas las maracamos con R
contador_reinas = 0 # contador de reinas colocadas
contador_soluciones = 0 # contador de soluciones encontradas, para tablero de 8x8 es 92


def mostrar_matriz(x): # funcion para mostrar cualquier matriz con "casillas"
    for i in x:         
        for j in i:     
            print(j+' | ', end=' ')
        print('')


# La siguiente funcion recive como parametro, el tablero, y las coordenadas  i j
# donde se pretende colocar una reina.
# se encarga de verificar si es prudente hacerlo, segun las reglas de 8 reinas
# que ninguna reina amenazca a otra. 
# retorna true en caso de no haber ningun problema, de haberlo retorna false

def verificar(l, i,j):
    aux1=i; aux2 =j
    
    # verifica verticalmente
    for z in range(8):
        if(l[z][j]=="R"): return False
    #verifica horizontalmente
    for z in range(8):
        if(l[i][z]=="R"): return False
    
    #verifica su diagonal derecha (nor este)
    while(True):
        i-=1; j+=1
        if(i<0 or j>7): break
        if(l[i][j]=="R"): 
            return False
        
    i=aux1; j=aux2;
    # verifica su diagonal izquierda (nor oeste) 
    while(True):
        i-=1; j-=1
        if(i<0 or j<0): break
        if(l[i][j]=="R"): 
            return False

    return True


# Funcion donde mediante bactracking se termina imprimiendo la solucion encontrada
# imprime las 92 distintas soluciones
def buscar_soluciones(l, i,j,colocado, contador_reinas):
    # el contador de soluciones es global, para que no se modifique
    # al acabarse ciertos ambientes recursivo
    global contador_soluciones


    # Si el contador de reinas es igual a 8, se encontro una solucion, se procede a imprimir
    if(contador_reinas == 8):
        contador_soluciones+=1
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
    while(i<8):
        j=0
        while(j<8):
            # se verifica si es prudente colocar la reina en la coordenada i j
            if(verificar(l,i,j)):
                l[i][j]=reina ; i+=1; aux=j; j=0
                contador_reinas+=1
                # en el siguiente condicional sucede el backtracking
                if(not buscar_soluciones(l,i,j ,False, contador_reinas)):
                    i-=1; j=aux
                    l[i][j]=" "; contador_reinas-=1
            # si no se coloco ninguna reina en la fila, es por anlgo anda mal
            # anteriormente se tuvo qeu tomar una mala desicion, se retornaria falso
            # matando el ambiente actual, el condicional de arriba en el ambiente anterior
            # se cumploria y se borraria la ultima reina colocada, buscando otras posibilidades
            if(j==7 and  not (i+1)==contador_reinas):
                return False
            j+=1
        i+=1

# Los argumentos son, la matriz l (tablero)
# indices i = 0, j = 0
# una variable que nos servira para saber si se ha colocado una reina en una fila
# se inicia en Falso
# y por ultimo se pasa el contador de reinas inicializados en 0
buscar_soluciones(l,0,0,False, 0)



input("Programa finalizado, presiente una tecla para terminar")