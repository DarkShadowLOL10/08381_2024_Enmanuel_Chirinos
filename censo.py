# censo.py
# Permite ingresar comunas y población por año, calcula estadísticas como promedio, máximos, mínimos y porcentajes.

import numpy as np

Comunas = []
Poblacion2015 = []
Poblacion2016 = []

Nc = int(input("Ingrese el número de comunas: "))

# Ingreso de datos para cada comuna
for i in range(Nc):
    Comunas.append(input(f"Comuna {i+1}: "))
    Poblacion2015.append(int(input("Población en 2015: ")))
    Poblacion2016.append(int(input("Población en 2016: ")))

print("\nComunas:", Comunas)
print("Población en 2015:", Poblacion2015)
print("Población en 2016:", Poblacion2016)

# Comuna con mayor población en 2016
lugar1 = Poblacion2016.index(max(Poblacion2016))
print(f"La comuna de mayor población para 2016 es {Comunas[lugar1]}, tenía {Poblacion2016[lugar1]} habitantes.")

# Comuna con menor población en 2016
lugar2 = Poblacion2016.index(min(Poblacion2016))
print(f"La comuna de menor población para 2016 es {Comunas[lugar2]}, tenía {Poblacion2016[lugar2]} habitantes.")

# Relación entre la comuna más habitada y la menos habitada
rmaxmin = Poblacion2016[lugar1] / Poblacion2016[lugar2]
print("Relación mayor/menor población:", round(rmaxmin, 2))

# Promedios y crecimiento
promedio2015 = np.mean(Poblacion2015)
promedio2016 = np.mean(Poblacion2016)
pcrecimiento = (promedio2016 - promedio2015) / promedio2015 * 100
print("Promedio de habitantes en 2015:", round(promedio2015, 0))
print("Promedio de habitantes en 2016:", round(promedio2016, 0))
print("Porcentaje de crecimiento regional:", round(pcrecimiento, 1), "%")

# Porcentaje de población por comuna en 2016
for i in range(Nc):
    porcentaje = Poblacion2016[i] / sum(Poblacion2016) * 100
    print(f"El porcentaje correspondiente a la comuna {Comunas[i]} es: {round(porcentaje, 1)}%")