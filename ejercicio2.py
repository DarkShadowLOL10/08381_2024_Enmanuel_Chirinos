usuario = str(input("indique su nombre: "))

Latitud = float(input("indique la latitud: "))
Longitud = float(input("indique la longitud: "))
distancia = float(input("indique la distancia: "))

area = (3.14*(distancia)**2)

print ("Estimado/a " + usuario+ " el area afectada  es: " + 
       str(area) + " considerando el foco, " + str(Latitud) + str(Longitud) + " , como punto central. ")