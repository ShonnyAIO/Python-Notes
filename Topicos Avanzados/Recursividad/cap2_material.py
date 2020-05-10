
# -------------- EJEMPLO1 ----------------------

# la función "pow" retorna el resultado de elevar x, y veces. (x   base)  (y exponente) 
def pow(x, y):
    if(0==y):
        return 1
    return x*pow(x,y-1)

#descomentar la siguiente línea para probar esta función
#print(pow(2,3))


# -------------- EJEMPLO2 ----------------------

# la función "al_reves"  imprime el string que se pasa como primer parametro al revés

def al_reves(s,x,t):
    if(t==0):
        print(x) ; return
    x+=s[t-1]
    al_reves(s, x, t-1)

#descomentar la siguiente linea para probar esta función
#s=input(); al_reves(s, "", len(s)) 



# -------------- EJEMPLO3 ----------------------


# esta función "es_palindromo", imprime un mensaje indicando si el string 
# del primer parametro es palindromo o no

def es_palindromo(string, li, lf):
    if(string[li]==string[lf]):
        print("es palindromo") ; return
    else:
        print("no es palindromo"); return 
    es_palindromo(string, li+1, lf-1)

#descomentar la siguiente linea para probar esta función
#string = input() ; es_palindromo(string, 0, len(string)-1)
    




# -------------- EJEMPLO4 ----------------------

#En este ejemplo se ve como una función recursiva se puede servir de otra funcion
#recursiva para lograr su objetivo, o que quizás entre ambas logren hacerlo. 


# programa que imprime los numeros desde 1 hasta el que numero que desee el usuario.

def pares(n, k): # imprme los pares
    if(n==k+1):
        return
    print(n, end=" ")  
    impares(n+1, k)

def impares(n, k): #imprime  los impares
    if(n==k+1):
        return
    print(n, end=" ")
    pares(n+1, k)

def print_numbers(k):  # un emboltorio, asi se le conoce a una función que solo se encarga de invocar a otra. 
    impares(1,k)


# Descomentar la proxima linea para ejecutar este programa
#x=int(input()) ; print_numbers(x)


# -------------- EJEMPLO5 ----------------------


# funcion recursiva que se encarga de determinar si un numero n, es primo
# retornara True en caso de ser así, en caso contrario retornara falso

def es_primo(n,k):
    
    if(n==1 or n==2): return True
    elif(n%k==0 and not k==1 and not n==k): return False
    elif(k>(n//2)+1): return True
    return es_primo(n, k+1)

# haciendo uso del siguiente algoritmo, se puede mostrar en pantalla
# los numeros primos, en un rango del 1 al 100
'''
for i in range(1,101):
    if(es_primo(i,1)):
        print(i, end=' ')
'''






# Para aprender otros lenguajes, practicar lo aprendido y expandir nuestras habilidades en programación
# hechar un vistazo a   hackerrank.com    portal con cientos  de retos de programación.