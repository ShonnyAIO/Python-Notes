from os import system

class node():
    def __init__(self, dato):
        self.left = None
        self.right = None
        self.dato = dato

class arbol():
    def __init__(self):
        self.root = None
        
    def insert(self, a, dato):
        if a == None:
            a = node(dato)
        else:
            d = a.dato
            if dato < d:
                a.left = self.insert(a.left, dato)
            else:
                a.right = self.insert(a.right, dato)
        return a

    def buscar(self, dato, a):
        if a == None:
            return None
        else:
            if dato == a.dato:
                return a.dato
            else:
                if dato < a.dato:
                    return self.buscar(dato, a.left)
                else:
                    return self.buscar(dato, a.right)

tree = arbol()

while True:
    system("cls")
    print("Árbol binario de búsqueda")
    opc = input("\n <1> Insertar nodo \n <2> Buscar \n <3> Salir \n\nElige una opcion: ")

    if opc == '1':
        nodo = int(input("\nIngresa un numero (nodo): "))
        tree.root = tree.insert(tree.root, nodo)
        
    elif opc == '2':
        nodo = int(input("\nIngresa el nodo a buscar -> "))
    
        nodo = int(nodo)
        if tree.buscar(nodo, tree.root) == None:
            print("\nNodo no encontrado...")
        else:
            print("\nNodo encontrado -> ",tree.buscar(nodo, tree.root), " si existe...")
            
    elif opc == '6':
        print("\nElegiste salir...\n")
        os.system("pause")
        break
    else:
        print("\nElige una opcion correcta...")
    print()
    system("pause")

print()