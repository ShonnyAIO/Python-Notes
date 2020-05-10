#Se busca hacer un programa en donde se gestione información sobre personas

#se pudo haber hecho manipulando archivos, de esa forma
#la informacion no se pierde luego de apagar el programa

# la logica de este programa es almacenar objetos de la clase persona
# en una lista.  Se le muestra al usuario un  menu, deonde puede escoger
# entre crear un nuevo regristro de una persona o buscar un registro ya 
# creado. 

class persona:
    def __init__(self, a,b,c,d,e):      #metodo constructor
        self.__cedula=a
        self.__nombre=b
        self.__edad=c
        self.__oficio=d
        self.__genero=e

    def mostrar_datos(self):            #metodo para mostrar datos
        print(f"Cedula: {self.__cedula}")
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"Oficio: {self.__oficio}")
        print(f"Genero: {self.__genero}")
    
    def cedula(self):                   # retornar identificacion, servira para buscar cierta persona
        return self.__cedula
    
l=[]        #lista para guardar los objetos de la clase



def buscar(x):  # x  contiene la cedula de la persona a buscar
    global l; # con global podemos trabajar con variables y listas definidas anteriormente
    # notar que necesitamos buscar en la lista l  a la persona dueña de la cedula que
    # se paso a esta funcion 


    for i in l:
        
        if(i.cedula() == x):
            i.mostrar_datos(); break
    #se reccorio la lista, hasta encontrar el objeto que contuviera dicha cedula
    #luego de encontarlo se utiliza su metodo mostra_datos




# algoritmo principal del programa

while(True):
    print("Crear registro de persona:                                 <1>")
    print("Buscar informacion acerca de una persona                   <2>")
    print("Salir                                         <cualquier otro caracter>")
    opcion=input()

    if(opcion == '1'):
        print("Ingresar cedula: "); a=input()
        print("Ingresar nombre: "); b=input()
        print('Ingresar edad: '); c=input()
        print("Ingresar oficio: "); d=input()
        print("Ingresar genero: "); e=input()
        obj = persona(a,b,c,d,e)   # creando objeto persona,  utilizando el constructor
        l.append(obj)  # ingresar objeto a la lista

    elif(opcion == '2'):
        print("Ingrese la cedula de la persona a buscar: "); a=input()
        buscar(a)
    else:
        break