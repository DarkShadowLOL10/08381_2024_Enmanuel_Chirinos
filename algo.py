# algo.py
# Calcula el promedio y la varianza de una lista de 5 números introducidos por el usuario.
# Muestra también cómo manejar listas de estudiantes y recorrer sus elementos.

# Inicialización de lista y variable acumuladora
valores = [0, 0, 0, 0, 0]
acc = 0

# Solicitar 5 valores al usuario
for i in range(5):
    valores[i] = int(input(f"Ingrese el número {i+1}: "))
    acc += valores[i]

print("Valores ingresados:", valores)

# Calcular promedio
promedio = acc / 5
print("Promedio:", promedio)

# Calcular varianza
suma_cuadrados = 0
for i in range(5):
    suma_cuadrados += (valores[i] - promedio) ** 2
varianza = suma_cuadrados / 5
print("Varianza:", varianza)

# Ejemplo de listas con datos de estudiantes
enmanuel = ["Enmanuel", 19, 5.5, True]
alonso = ["Alonso", 19, 5.5, True]
estudiantes = [alonso, enmanuel]

# Recorrido de la lista de estudiantes para mostrar sus nombres
for estudiante in estudiantes:
    print("Nombre del estudiante:", estudiante[0])