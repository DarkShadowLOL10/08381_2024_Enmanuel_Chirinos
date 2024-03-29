# ingresamos el nombre del usuario #
usuario = str(input("indique su nombre: "))

# ingresar longitud, lagitud, y la distancia #
Latitud = int(input("indique la latitud: "))
Longitud = int(input("indique la longitud: "))
distancia = int(input("indique la distancia: "))

# Se calcula el area del perimetro #
area = (3.14*(distancia)**2)


print ("Estimado/a usuaria/o " + str(usuario) + ", el area afectada  es: (" + 
       str(area) + ") considerando el foco, (" + str(Latitud) + "), (" + str(Longitud) + "), (" 
       + str(distancia) + "KM), como punto central.")
