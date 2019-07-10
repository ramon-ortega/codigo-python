#Aqui llamamos nuestro modulo


import validador
from validador import validate_email

email = 'prueba@gmail.com'
if validate_email(email):
	print('El correo esta bien escrito')
else:
	print('El correo esta mal escrito')
