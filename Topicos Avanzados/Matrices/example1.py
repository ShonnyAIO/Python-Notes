# Este es un programa en donde se imprime una matriz de numeros enteros
# El usuario elige la cantidad de columnas y filas
# El usuario ingresa los numeros enteros
# Si la matriz es cuadrada, es decir si tiene tantas filas como columnas, se mostrara la suma de todos los numeros enteros
# de la diagonal principal



l = [] # lista donde se creara la matriz


print("Ingrese las dimensiones de la matriz de numeros enteros: ")
col = int(input("numero de columnas: "))
fil = int(input("numero de filas: "))

# se pide al usuario los numeros enteros que contendra la matriz

print("Ingrese los numeros enteros: ")
for i in range(fil):
    m = []
    for i in range(col):
        m.append(int(input()))
    l.append(m)    

# Se imprime la matriz 
print("Matriz:\n")

for i in l:         
    for j in i:     
        print(str(j)+' |', end=' ')
    print('')

# Si la matriz es cuadrada, es decir si tiene tantas filas como columnas, se mostrara la suma de todos los numeros enteros
# de la diagonal principal

if( fil == col):
    print("\nSuma de los numeros de la diagonal")
    print("(de la esquina superior izquierda a esquina inferior derecha)\n")
    suma=0
    for i in range(fil):
        suma += l[i][i]
    print(f"resultado: {suma}")




