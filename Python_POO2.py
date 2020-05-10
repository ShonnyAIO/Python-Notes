"""
class A:
	__x = 17 ; __y = 16
	def imprimir_variables(self):
		#print(f'x = (self.x) y =  (self.y)' )
		print("x =", (self.__x))
		print("y =", (self.__y))


objeto = A()
objeto.x = 5 ; objeto.y = 19
objeto.imprimir_variables()
"""
"""
class personaje:

	def __init__(self, a,b,c):
		self.__nombre = a
		self.__vida = b
		self.__fuerza = c

	def mostrar_datos(self):
		print("Nombre: ", self.__nombre)
		print("Vida: ", self.__vida)
		print("Fuerza: ", self.__fuerza)

a = personaje("Kratos", 1000, 9000) ; a.mostrar_datos()
b = personaje("Thor", 2000, 5000) ; b.mostrar_datos()
"""
class Banco:
	def __init__(self, x):
		self.__dinero = x

	def boveda(self, x):
		self.__dinero = x

	def dinero_del_banco(self):
		return self.__dinero

class Ladron:
	__dinero = 0

	def robar(self, t):
		self.__dinero += t.dinero_del_banco()
		t.boveda(0)

	def dinero_del_ladron(self):
		print("Dinero del ladron ", self.__dinero)

banco1 = Banco(400) ; ladron1 = Ladron()

ladron1.dinero_del_ladron() ; print("Dinero del banco: ", banco1.dinero_del_banco())
ladron1.robar(banco1) ; print("Robo realizado")
ladron1.dinero_del_ladron() ; print("Dinero del banco: ", banco1.dinero_del_banco())