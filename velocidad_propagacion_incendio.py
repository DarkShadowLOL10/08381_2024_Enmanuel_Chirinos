# Script para calcular la velocidad de propagación de un incendio entre dos posiciones geográficas.
# Solicita nombre, coordenadas iniciales y finales, y tiempos.

usuario = str(input("Indique su nombre: "))  # Nombre del usuario

# Coordenadas iniciales
lat1 = int(input("Indique la latitud (inicial): "))
lon1 = int(input("Indique la longitud (inicial): "))

# Coordenadas finales
lat2 = int(input("Indique la latitud (final): "))
lon2 = int(input("Indique la longitud (final): "))

# Cálculo de distancia usando el teorema de Pitágoras
dist_km = int(((lon2 - lon1) ** 2 + (lat2 - lat1) ** 2) ** 0.5)
dist_mts = dist_km * 1000

# Solicitar tiempos de propagación
time_horas1 = int(input("El tiempo en la cual inició la propagación del fuego (horas): "))
time_horas2 = int(input("El tiempo en la cual se propagó en la distancia (horas): "))

time_seg1 = time_horas1 * 3600
time_seg2 = time_horas2 * 3600

# Cálculo del tiempo total en segundos y velocidad
time_promedio = time_seg2 - time_seg1
velocidad = dist_mts / time_seg1

print(f"Estimado/a usuaria/o ({usuario}), la velocidad de propagación del incendio iniciado en "
      f"({lat1}), ({lon1}), es de ({velocidad}) m/s.")