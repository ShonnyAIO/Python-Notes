x = lambda a,b,c: a%2==0 and b%2==0 and c%2==0

print("Ingrese 3 enteros pares: ")
while(True):
    try:
        #a=5
        if x( 
            int(input("Primer entero: ")),
            int(input("Segundo entero: ")),
            int(input("Tercer entero: "))
        ):
            print("exito"); break
        else:
            print("Vuelva a intentarlo"); continue
    except Exception as ex:
        print(f"Ha ocurrido un error {ex}")
        print("Vuelva a intentarlo")

#print(a)
# notar que x, nuestra función lambda, retornará True sí y solo sí sus 3 argumentos son numeros pares
# notemos que el if evalua el booleano que retorne tal funcion. 
# el break se usa para finalizar el ciclo while y se ejecutará siempre y cuando
# no haya ocurrido alguna excepción. 
# Notar tambien que si creamos variables en el try, podremos acceder a ellas aun afuera del ciclo


from random import randint
# En funciones lambdas, luego de los dos puntos podemos 
# invocar funciones, en el siguiente ejemplo se retornaria el producto de los
# enteros que retornen esas funciones
c = lambda : int(input())*randint(1,100)
print(c())  #imprimiendo lo que retorna c