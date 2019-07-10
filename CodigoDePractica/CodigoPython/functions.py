#funcion es un bloque de codigo que solo corre cuando se le llama


#crear una funcion, esta funcion no regresa nada solo imprime

def decirHola(nombre=' '):
	print('Hola {0}'.format(nombre))

decirHola('Ramon')
decirHola()

#funcion que me regresa un valor

def hacerSuma(num1, num2):
	total = num1+num2
	return float(total)

hacerSuma(2,3)
print(hacerSuma(2,3),type(hacerSuma(2,3)))

x=2
y=2
total = hacerSuma(x,y)
print(total, type(total))
