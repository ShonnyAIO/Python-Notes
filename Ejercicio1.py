x = int(input()); lista1 = []; lista2 = []

for i in range(x):
    string = input()
    lista1.append(input())
    if(lista1[i] in string):
        cont=0
        for a in string:
            if(a==lista1[i]): cont+=1
        lista2.append(cont)
    else: lista2.append(0)

for i in range(x):
    print(f"En la cadena de caracteres #{i+1} el caracter '{lista1[i]}', aparece {lista2[i]} veces")