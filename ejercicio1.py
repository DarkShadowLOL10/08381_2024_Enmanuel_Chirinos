# ejercicio1.py
# Calcula el promedio de consumo de comida de una familia durante 3 días.

usuario = str(input("Indique su nombre: "))  # Nombre del usuario
Dia1 = float(input("Comida consumida del día 1: "))
Dia2 = float(input("Comida consumida del día 2: "))
Dia3 = float(input("Comida consumida del día 3: "))

promedio = (Dia1 + Dia2 + Dia3) / 3

print(f"Estimado/a {usuario}, su promedio de consumo es: {promedio}")