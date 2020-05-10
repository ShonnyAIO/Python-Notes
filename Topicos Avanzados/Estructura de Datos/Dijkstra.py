from math import inf
# inf infinito positivo

# se modelara el grafo con un diccionario
# el nombre de cada vertice sera una clave distinta que guardara una lista donde estaran sus adyacentes
# la lista contendra tuplas de la forma:  (vertice_adyacente, distancia/costo)
grafo = dict()
numero_vertices=0
vertice_de_partida = ""

# esta funcion lee la informacion del grafo contenido en el archivo entrada.txt
def entrada():
    global grafo; global numero_vertices

    archivo = open("entrada.txt", "r")
    numero_vertices=int(archivo.readline().strip("\n"))
   
    for i in range(numero_vertices):
        nombre_vertice = archivo.readline().strip("\n")
    
        adyacentes = list(archivo.readline().split())
        
        lista_adyacentes=[]

        for j in range(0,len(adyacentes), 2):
            lista_adyacentes.append(   (adyacentes[j], int(adyacentes[j+1]) )   )
            
        grafo[nombre_vertice]=lista_adyacentes



# esta funcion recursiva ayudara a acomodar la ruta optima a cada vertice
def retornar_ruta(rutas_optimas, vertice):
    if(rutas_optimas[vertice] is vertice_de_partida):
        return rutas_optimas[vertice] 
    return retornar_ruta(rutas_optimas, rutas_optimas[vertice])+" --> "+rutas_optimas[vertice]


# con esta funcion se imprime los resultados
def imprimir_solucion(rutas_optimas, distancias_minimas):
    for vertice in grafo:
        if vertice is vertice_de_partida: continue
        print(f"El menor costo para llegar al vertice {vertice} es: {distancias_minimas[vertice]}")
        print(f"La ruta optima entonces seria: {retornar_ruta(rutas_optimas, vertice)} --> {vertice}")
    pass


def dijkstra(nombre_nodo_inicial, grafo):
    #"distancias minimas", tomemoslo como "costo minimo" para viajar a ese vertice desde el inicio
    # en este caso seria un diccionario que la clave seria el nombre del vertice, y el dato el costo
    # seria como nuesta estructura "D" que se menciono en el pdf
    distancias_minimas = dict(); visitados = set()
    rutas_optimas=dict();  # aqui se guardaran los nombres de los vertices pertenientes a las rutas mas baratas
    #en el conjunto visitados, se dejaran los nombres de los vertices que valga la redundancia, hayan sido visitados
    for i in grafo:
        
        if i is nombre_nodo_inicial :
            distancias_minimas[i] = 0
            rutas_optimas[i]=nombre_nodo_inicial
            visitados.add(i)
        else:
            distancias_minimas[i] = inf  # se setea las distancias en infinito 
            rutas_optimas[i]=""
         

    vertice_actual = nombre_nodo_inicial

    while(not len(visitados) is numero_vertices):

        for vertice in grafo: # se recorre cada vertice del grafo

            if vertice is vertice_actual :
                
                for vecino in grafo[vertice]: #vecino, tomemoslo como sinonimo de "adyacente"
                    #vecino seria cada tupla ( vertice_adyacente, costo/distancia)
                    #  vecino[0] = nombre, vecino[1]=distancia/costo
                    distancia_a_vecino = distancias_minimas[vertice]+vecino[1]
                    
                    if distancias_minimas[vecino[0]] > distancia_a_vecino:
                        distancias_minimas[vecino[0]] = distancia_a_vecino
                    
                        rutas_optimas[vecino[0]]=vertice
                        
                #se deja en la variable menor_distancia, el entero que sea el menor costo
                #se ignora los el costo para viajar a los vertices visitados
                # ya que el proximo vertice_actual sera el que tenga menor costo y que no haya sido visitado  
                menor_distancia = min (
                    tuple(distancias_minimas[j]  
                          for j in distancias_minimas 
                          if not j in visitados)
                )
                
                for i in distancias_minimas:
                    if distancias_minimas[i] is menor_distancia and i not in visitados:
                       
                        vertice_actual=i  ; visitados.add(i); break
                break
    # ya dijkstra hizo su trabajo ahora se imprimira la solucion
    imprimir_solucion(rutas_optimas, distancias_minimas)


entrada()
vertice_de_partida=input("Ingrese el nombre del vertice de partida: ")
dijkstra(vertice_de_partida, grafo)
input()