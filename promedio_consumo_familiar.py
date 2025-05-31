# Script para calcular el promedio de consumo de comida de una familia durante 3 días.
# Solicita el nombre del usuario y los consumos diarios, luego muestra el promedio.

usuario = str(input("Indique su nombre: "))  # Nombre del usuario

# Solicitud de los consumos diarios
Dia1 = float(input("Comida consumida del día 1 de su familia: "))
Dia2 = float(input("Comida consumida del día 2 de su familia: "))
Dia3 = float(input("Comida consumida del día 3 de su familia: "))

# Cálculo del promedio de consumos
promedio = (Dia1 + Dia2 + Dia3) / 3

# Mostrar resultado por pantalla
print(f"Estimado/a {usuario}, su promedio es: {promedio} del consumo de su familia del día.")