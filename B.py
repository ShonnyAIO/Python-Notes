# Programa que simula una batalla entre dos ejercitos
# El usuario ingresara una serie de datos para cada ejercito
# Se mostrara en la salida, los datos del ejercito vencedor
# el ejercito vencedor es el que tenga mas "sobrevivientes" luego de la batalla
# el usuario ingresara la cantidad de soldados (infanteria), tanques (artilleria) y aviones (aviacion)
# y luego la cantidad de bajas  


# La razon de este codigo es ver como una clase puede tener como atributos objetos de otra clase
# La clase "Ejercito", tiene atributos que son objetos  de las clases "Infanteria", "Artilleria" y "Aviacion"


class Infanteria:    

    def __init__(self, a):    
        self.__cantidad_soldados = a

    def calcular_bajas(self, a):       
        x =  self.__cantidad_soldados*(a/100)
        self.__cantidad_soldados -= x
        return x
    
    def cantidad_sobrevivientes(self): 
        return self.__cantidad_soldados


class Aviacion:
    def __init__(self, a):
        self.__cantidad_aviones = a
        
    def calcular_bajas(self, a):
        f =  self.__cantidad_aviones*(a/100)
        self.__cantidad_aviones -= f
        return f
    
    def cantidad_sobrevivientes(self):
        return self.__cantidad_aviones



class Artilleria:
    def __init__(self, a):
        self.__cantidad_morteros = a
        
    def calcular_bajas(self, a):
        f =  self.__cantidad_morteros*(a/100)
        self.__cantidad_morteros -= f
        return f
    
    def cantidad_sobrevivientes(self):
        return self.__cantidad_morteros


# clase ejercito, los metodos de esta clase se usaran bastante en el algoritmo principal del programa

class Ejercito:
    # constructor en donde se pasaran como argumentos, el nombre, la cantidad de infanteria
    # la cantidad de artilleria, cantidad de aviacion y lema del ejercito
    def __init__(self, a,b,c,d, f): 
        self.__nombre = a
        self.__sobrevivientes = 0
        self.__infanteria = Infanteria(b)
        self.__artilleria = Artilleria(c)
        self.__aviacion = Aviacion(d)
        self.__cantidad_total = b+c+d
        self.__lema_del_ejercito = f
    
    def obtener_bajas(self):
        # se le pide al usuario en porcentaje la cantidad de bajas en cada elemento del ejercito y luego se calcula la cantidad de sobrevivientes
        print("\nIngresar la cantidad de bajas de la infanteria en porcentanje (de 0 a 100): ", end=' ')
        f=int(input())
        bajas_totales = self.__infanteria.calcular_bajas(f)
     
        print("\nIngresar la cantidad de bajas de la artilleria en porcentanje (de 0 a 100): ", end=' ')
        f=int(input())
        bajas_totales += self.__artilleria.calcular_bajas(f)
     
        print("\nIngresar la cantidad de bajas de la aviacion en porcentanje (de 0 a 100): ", end=' ')
        f=int(input())
       
        bajas_totales += self.__aviacion.calcular_bajas(f)
       
        self.__sobrevivientes = self.__cantidad_total - bajas_totales

    def sobrevivientes(self):   # retorna la cantida de sobrevivientes
        return self.__sobrevivientes

    def reporte_sobrevivientes(self):   # imprime la cantidad de sobrevivientes en  cada elemento del ejercito
        
        print("\nSobrevivientes de la infanteria: ", end='')
        print(self.__infanteria.cantidad_sobrevivientes())

        print("\nSobrevivientes de la aviacion: ", end='')
        print(self.__artilleria.cantidad_sobrevivientes())

        print("\nSobrevivientes de la artilleria: ", end='')
        print(self.__aviacion.cantidad_sobrevivientes())

        print("\nSobrevivientes totales:", self.__sobrevivientes)
    
    # retornar lema y nombre
    def lema(self):
        return self.__lema_del_ejercito
    
    def nombre(self):
        return self.__nombre


l=[] # lista donde se guardaran 2 objetos  de la clase ejercito luego de adquirir sus respectivos datos

def adquirir_datos():  # con esta funcion se le pide al usuario los datos pertinentes para cada objeto de la clase ejercito
    global l

    print("\nNombre del ejercito: ", end=' ')
    nombre = input()

    print("\nCantidad de soldados (infanteria): ", end=' ')
    cantidad_infanteria = int(input())

    print("\nCantidad de tanques y morteros (artilleria): ", end=' ')
    cantidad_artilleria = int(input())

    print("\nCantidad de aviones (fuerza aerea): ", end=' ')
    cantidad_aviones = int(input())
    
    print("\nIngrese lema del ejercito: ", end=' ')
    lema = input()

    obj = Ejercito(nombre, cantidad_infanteria, cantidad_artilleria, cantidad_aviones, lema) # se crea el objeto
    l.append(obj)    # se agrega el objeto a la lista


# algoritmo principal del programa
for i in range(2):
    if(i==0): print("Ingrese los dados del 1er ejercito: ")
    else: print("\nIngrese los datos del 2do ejercito: ")
    adquirir_datos()
    l[i].obtener_bajas() # notar que de esta manera tambien podemos acceder al objeto anteriormente ingresado en la lista


# ahora se evalua cual ejercito salio victorioso de la batalla
# recordar que en la lista  "l" estan almacenados los dos objetos de la clase ejercito creados
if(l[0].sobrevivientes() > l[1].sobrevivientes()):
    print(f"\nEjercito ganador: {l[0].nombre()}")
    print(f"Lema del ejercito: {l[0].lema()}")
    print("Reporte de sobrevivientes: ")
    l[0].reporte_sobrevivientes()

elif(l[0].sobrevivientes() < l[1].sobrevivientes()):
    print(f"\nEjercito ganador: {l[1].nombre()}")
    print(f"Lema del ejercito: {l[1].lema()}")
    print("Reporte de sobrevivientes: ")
    l[1].reporte_sobrevivientes()

else:
    print("Ningun ejercito salio victorioso")