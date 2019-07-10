#una clase es como un plano para crear objetos, un objeto tiene propiedades y metodos asociadas a el.

#creando una clase

class Usuario:
#Constructor -funcion que corre cuando haces una instanciacion de una clase

	def __init__(self, nombre, email, edad):
		self.nombre = nombre
		self.email  = email
		self.edad = edad

	def saludos(self, num1=1):
		print(num1)
		return 'Me llamo {0} y tengo {1} y mi correo es {2}'.format(self.nombre,self.edad, self.email)

	def tengo_cumple(self):
		self.edad+=1

#Init un objeto para el usuario
Ramon = Usuario('Ramon Ortega', 'ramon@gmail.com', 25)
print(type(Ramon))
print(Ramon.nombre)
print(Ramon.saludos(1))

Ramon.tengo_cumple()
print(Ramon.saludos())

#NUEVA CLASE

#Extender la clase del usuario
class Cliente(Usuario): 
	#Constructor (funcion que corre cuando haces una instanciacion de una clase)
	def __init__(self, nombre, email, edad):
		self.nombre = nombre
		self.email = email
		self.edad = edad
		self.saldo = 0

	def establecersaldo(self,saldo):
		self.saldo = saldo

	def saludos(self):
		return 'Me llamo {0}, tengo {1}, mi correo es {2} y mi saldo es {3}'.format(self.nombre,self.edad,self.email,self.saldo)

print('------------------------------------')

#Init un objeto para el usuario
Rufina_usuario = Usuario('Rufina Madrid', 'rufina@gmail.com', 34)
Rufina_cliente = Cliente('Rufina Madrid', 'rufina@gmail.com', 34)
Rufina_cliente.establecersaldo(10)
print(Rufina_cliente.saludos())
print(Rufina_usuario.saludos())
