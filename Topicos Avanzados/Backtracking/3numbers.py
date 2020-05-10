
print("\nPrograma que busca 3 numeros enteros positivos a, b y c  tal que: cada uno elevado al cubo")
print("y luego sumados de como resultado el numero que usted va a ingresar")
print("a, b y c  son unicos, no se repiten  y estan dentro de un rango de 1 al 20")
print("Se utilizara la tecnica de backtracking")
print("Es posible que con el numero que ingrese no exista solucion")
# ejemplos de numeros con los que existe solucion:  36, 8513, 2330


# funcion que me ayudara a verificar si el conjunto candidato con el que se esta tanteando es solucion
def solucion(conjunto_candidato, number):
    suma = 0
    for i in conjunto_candidato:
        suma += i**3
    return suma == number


contador_soluciones = 0


def busqueda(lista, number, conjunto_candidato, t, i):
    global contador_soluciones

    # si y solo si el conjunto ya tiene 3 numeros es que se verificara si es solucion
    if(len(conjunto_candidato) == 3):
        if(solucion(conjunto_candidato, number)):
            # se imprime la solucion encontrada
            contador_soluciones += 1
            print(f"Solucion encontrada:")

            for i in conjunto_candidato:
                print(i, end=" ")
        else:
            # esto significa que mi conjunto candidato no es solucion, se devuelve falso, matando este ambiente
            # retornamos a un ambiente pasado
            return False
    else:
        while(i < t):
            conjunto_candidato.add(lista[i])
            # en el siguiente condicional se invoca recursivamente la funcion, precedido de un "not"
            # para generar la tecnica de backtracking, en caso de retornar falso, se borra el numero colocado
            # y se prueba con otro seguramente mayor.
            if(not busqueda(lista, number, conjunto_candidato, t, i+1)):
                conjunto_candidato.remove(lista[i])
                i += 1


# creo un conjunto vacio, donde voy a ir colocando los numeros candidatos
conjunto_candidato = set()
number = int(input("\nIngrese un numero entero positivo: "))
# creo una lista de numeros del 1 al 20
lista = [i for i in range(1, 21)]
# invoco la funcion del backtracking
busqueda(lista, number, conjunto_candidato, 20, 0)
if(contador_soluciones == 0):
    print("No se encontro solucion")


input("Programa finalizado, presiente una tecla para terminar")