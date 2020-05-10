"""
Es una estructura propia de Python que tiene las siguientes caracteristicas particulares:
- NO se puede recorrer mediante indices
- NO se admiten elementos repetidos

"""


figuras = {"cuadrado", "circulo", "triangulo"}
print(figuras)


figuras.add("trapecio")
print(figuras)
figuras.remove("circulo")
print(figuras)
figuras.add("cuadrado")
print(figuras)

for i in figuras:
	print(i, end=" ")

a = "triangulo" in figuras #True
b = 4.1 in figuras # False

print({2,4,6, 'abc'} - {2,4, 'abc'}) # A - B

print({True, 2, False, 1} & {"a", "z", False, 2}) # A intersección B, deben ser comunes

print({1,2,3} | {2,4,5}) # Union A v B (Se incluyen todos)

print({1,2,3} {2,4,5}) #XOR P -> Q, los que se repiten no se incluyen