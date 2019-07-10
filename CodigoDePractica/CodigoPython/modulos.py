#un modulo es basicamente un archivo que contiene un conjunto de funciones que puedes incluir en tu codigo

#Importar un modulo de python que tiene por default

#Import--> palabra clave para llamar a un modulo
#Datetime-> libreria ya establecida
#es la primera vez que vamos a importar una libreria de python
#no es una libreria ligada al archivo por lo tanto la tenemos que llamar

import datetime
hoy=datetime.date.today()
print(hoy)

#from, llamamos, y lo unico que nos importa es hoy, una forma similar a la pasada pero mas elegante
from datetime import date
hoy2= date.today()
print(hoy2)

#Todavia se puede hacer mas elegante, llamamos time y lo llamamos estampa temporal
import time
estampatemporal =time.time()
print(estampatemporal)

#Mas elegante todavia
from time import time
estampatemporal2 = time()
print(estampatemporal2)

#administrador para instalar modulos externos
#modulo camel cas
#pip --version
#pip install camel case
#pip freeze 
 
#from camelcase import Camel Case

#instancion o instancia de camel case

#c = CamelCase()
#print(c.hump('hola otra vez mundo'))

#Modulo personalizado
import validador
from validador import validate_email

email ='prueba@'
if validate_email(email):
	print('El correo esta bien escrito')
else:
	print('El correo esta mal escrito')
