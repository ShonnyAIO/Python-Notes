# funcionas lambdas, anonimas
# Tambien estan en C, JS, PHP, PERL, GO, etc
"""
def sumar37(x):
	return x+37
"""

# sumar37 = lambda x: x+37

#a = int(input())+37

#a = sumar37(int(input()))
#print(a)

"""
h = lambda x,y,z: (2*x)+(y*z)
h = lambda : 2
h = lambda x: f"¡{str(x)}!"
"""

y = lambda x, k: x.title()+" "+k.title()

a = [y(input("Ingresar nombre: "), input("Ingresar Apellido: "))
	for i in range(int(input("Ingresar cantidad: ")))]
print(a)


def div_a_b(a,b):
	return lambda x: (a+b)/x

print(div_a_b(2,6)(4))