class A:
	def __init__(self, a,b):
		self.x = a
		self.y = b

	def print1(self):
		print(1)


#La clase B es hija de A
class B(A):

	def datos(self):
		print("Atributos heredados: ", self.x, self.y)

	def print2(self):
		print(2)

# objeto = B('abc', 5); objeto.print1() ; objeto.print2(); objeto.datos()

class C:
	def metodo(self, a):
		print(a)

class D:
	def __init__(self, t):
		self.variable = t

	def metodo(self ,b,c):
		print(b,c)

class E(C,D):
	def metodo(self):
		print(self.variable)

#objeto = E(16) ; objeto.metodo()


class Persona:
	def __init__(self,x,y):
		self.nombre = x
		self.edad = y

	def saludar(self):
		print("Hola :D")

	def despedir(self):
		print("Hasta luego")

class Profesor(Persona):

	def __init__(self, a,b,c):
		Persona.__init__(self,a,b)
		self.__asignatura = c

	def datos(self):
		print("Datos del profesor: \n", "Nombre: ", self.nombre , "Edad: ", self.edad, "Materia: ", self.__asignatura)


e = Profesor("Daniel", 30, "Programacion")
e.saludar()
e.datos()
e.despedir()