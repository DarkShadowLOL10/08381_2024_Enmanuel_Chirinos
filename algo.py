# Necesitamos un varchart que se almacene todos los valores #
# i manda los valores #
acc = 0
valores = [0, 0, 0, 0, 0]
print(valores)
 
for i in [1, 2, 3, 4]:
 
    valores[ i-1 ] = int(input("Ingrese el número:  " + str(i) + ": "))
    acc = acc + valores[i-1]
    print(i)
 
print(valores)
promedio = acc/5
print(promedio)
 
acc = 0
for i in [0, 1, 2 ,3, 4]:
    acc = (acc + (valores[i] - promedio)**2)
 
varianza = acc/5
print(varianza)
 
# El i-1 arregla posicion 1 como un 0 ex valores [ i-1 ] #
# ahora calcularemos la variante el valor - el proemdio **2 y sumatoria
 
# ejercicio: #
#  x1 = 1
#x2 = 2
#x3 = 3
#x4 = 4
#x5 = 5
#x = (x1 + x2 + x3 + x4 + x5)/5
#z = ((x1-x)**2+(x2-x)**2+(x3-x)**2+(x4-x)**2+(x5-x)**2)/5
#X = 5
#if (z<X) & (z<x):
#    print("algo por aquí")
#else:
#    print("otra cosa por acá")
#print(z) #
 
#estudiantes: nombre, edad, promedio, aprobacion
 
enmanuel = ["Enmanuel", 19, 5.5, True]
alonso = ["Alonso", 19, 5.5, True]
estudiantes = [alonso, enmanuel]
#tiene menú contextual#

for i in [0, 1]:
    e = estudiantes[i]
    print(e[0])

