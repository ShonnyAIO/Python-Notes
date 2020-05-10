# En este codigo vemos un ejemplo de herencia
# Las clases "moto" y "avion" heredan los atributos y metodoos de la clase "Vehiculo"
# Se recomienda analizar este codigo  y editarlo si se quiere para comprender bien el proceso de herencia

class vehiculo:
    def __init__(self):
        self.tipo = ''
        self.encendido = False
        self.capacidad_max_pasajeros = 0
        self.pasajeros = []
        self.vel_max = 0    
    
    def mostrar_pasajeros(self):
        for i in self.pasajeros:
            print(i, end=' ')
        print("")
    
    def mostrar_vel_max(self):
        print(self.vel_max)
    
    def encender_apagar(self):
        self.encendido = not self.encendido
    
    def estado(self):
        if(self.encendido):
            print("Esta encendido")
        else:
            print("Esta apagado")

    def reporte_general(self):
        print("Vehiculo: ")
        print(self.tipo)
        print("Estado: ")
        self.estado()
        print("Pasajeros: ")
        self.mostrar_pasajeros()
        print("Velocidad maxima: ")
        self.mostrar_vel_max()
        

class moto(vehiculo):
    
    def __tipo(self):
        self.tipo="Moto"

    def __velMax(self):
        self.vel_max = "200 km/h"

    def ingresar_pasajeros(self):
        self.__tipo()
        self.__velMax()
        for i in range(2):  # porque una moto tiene maximo 2 pasajeros
            print(f"Ingrese el nombre del pasajero #{i+1} :", end=' ')
            x=input()
            self.pasajeros.append(x)

class avion(vehiculo):
    
    def __tipo(self):
        self.tipo="Avion comercial"

    def __velMax(self):
        self.vel_max = "900 km/h"

    def ingresar_pasajeros(self):
        self.__tipo()
        self.__velMax()
        for i in range(200):  
            print(f"Ingrese el nombre del pasajero #{i+1} :", end=' ')
            x=input()
            self.pasajeros.append(x)
    

# obj=moto(); obj.ingresar_pasajeros(); obj.encender_apagar(); obj.reporte_general()