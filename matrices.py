archivo1 = open("matrices.txt", "r")
archivo2 = open("salida.txt", "w")
n = int(archivo1.readline())
t=0; l=[]
for i in range(n):
    dimension = int(archivo1.readline())
    for i2 in range(dimension):
        l = list(archivo1.readline().split())
        for i3 in l:
            if(int(i3)>t): t=int(i3)
    archivo2.write(f"numero mayor de la matriz #{i+1}: {t} \n"); t=0

archivo1.close(); archivo2.close()