# Script para calcular el área afectada por un incendio, tomando una ubicación central y un radio.
# Solicita nombre, latitud, longitud y distancia.

usuario = str(input("Indique su nombre: "))  # Nombre del usuario

# Solicitud de datos geográficos y distancia
Latitud = int(input("Indique la latitud: "))
Longitud = int(input("Indique la longitud: "))
distancia = int(input("Indique la distancia (radio en KM): "))

# Cálculo del área circular afectada
area = 3.14 * (distancia) ** 2

print(f"Estimado/a usuaria/o {usuario}, el área afectada es: ({area}) considerando el foco, "
      f"({Latitud}), ({Longitud}), ({distancia}KM) como punto central.")