# Ingresamos el nombre del usuario #
usuario = str(input("indique su nombre: "))

# Variables de 1 posicion de distancia #
lat1 = int(input("Indique la latitud (inicial): "))
lon1 = int(input("Indique la longitud (inicial): "))

# Variables de 2 posicion de distancia #
lat2 = int(input("Indique la latitud (final): "))
lon2 = int(input("Indique la longitud: (final): "))

# Distancia de la propagacion del incendio #
dist_km = int(((lon2 - lon1)**2 + (lat2 - lat1)**2)**(1/2))
dist_mts = int(dist_km * 1000)

# Tiempo de propagacion #
time_horas1 = int(input("El tiempo en la cual inicio la propagacion del fuego: "))
time_horas2 = int(input("El tiempo en la cual se propago en la distancia: "))

time_seg1 = int(time_horas1 * 3600)
time_seg2 = int(time_horas2 * 3600)
time_promedio = int(time_seg2 - time_seg1)

velocidad = (dist_mts/time_seg1)

print ("Estimado/a usuaria/o (" + str(usuario) + "), la velocidad de propagacion del incendio iniciado en (" + 
    str(lat1) + "), (" + str(lon1) + "), es de (" + str(velocidad) + ")")