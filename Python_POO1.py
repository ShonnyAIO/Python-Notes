"""
a = "murcielago"
print(a.upper())
b = "ABC"
print(b.lower())
"""


class Persona:
	edad = 20
	dinero = 500

	def saludar(self):
		print("Hola :D")

	def despedirse(self):
		print("Hasta luego")

	def vender(self):
		self.dinero += 250

	def mostrar_dinero_actual(self):
		print(self.dinero)

	def quiebra(self):
		self.dinero = 0

a = Persona()
a.edad = 50
print(a.edad)

#a.saludar()
#a.despedirse()
a.vender()
a.mostrar_dinero_actual()
a.quiebra()
a.mostrar_dinero_actual()