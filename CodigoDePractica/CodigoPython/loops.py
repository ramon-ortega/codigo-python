#simple loop7
people =['Ramon', 'Eduardo', 'Benito', 'Jorge', 'Karla']

print('*****Simple loop*****')
for person in people:
#   print "Current Person: ", person    #--> OTRA MANERA DE ESCRIBIRLO
   print('Current Person: {0}'.format(person))

#Break, repite hasta el valor que decimos
print('*****Break loop*****')
for person in people:
	if person == 'Benito':
	   break
	print('Curren Person: {0}'.format(person))

#Continue,es un loop donde no toma el valor de continue
print('*****Continue loop*****')
for person in people:
	if person == 'Ramon':
	 continue
	print('Curren Person: {0}'.format(person))

print('*****Range Loop*****')
#range, hace una lista con un rango
for i in range(len(people)):
	print(people[i])

for i in range(0,11):
	print('Number: {0}'.format(i))

#White loops: hasta que se cumpla una condicion:

print('*****Count*****')
count=0
while count <= 10:
	print('Count: {0}'.format(count))
	count+=1
