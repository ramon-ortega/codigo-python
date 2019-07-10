#Python tiene funciones para leer, actualizar y eliminar archivos

#Abrir un archivo

miArchivo = open('miArchivo.txt','w')

#Obtener informacion de este archivo

print('Name: ', miArchivo.name)
print('Esta cerrado: ', miArchivo.closed)
print('Modo abierto: ', miArchivo.mode)

#Escribir algo al archivo
miArchivo.write('Me encanta Python')
miArchivo.write(' y ROOT')
miArchivo.close()

#Agregar al archivo
miArchivo = open('miArchivo.txt','a')
miArchivo.write(' y tambien C++')
miArchivo.close()

#Leer un achivo
miArchivo = open('miArchivo.txt','r+')
texto = miArchivo.read(150)
print(texto)

#TAREA REVISAR LOS PROGRAMAS QUE HICIMOS
#APLICAR TODO LO APLICADO A ALGO
