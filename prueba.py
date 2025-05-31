# prueba.py
# Permite ingresar nombres y notas de varios estudiantes, calcula el promedio individual y general.
# Incluye comentarios para cada paso.

nombres_estudiantes = [] 
notas_estudiantes = []

Nc = int(input("Ingrese el número de estudiantes: ")) 

# Ingreso de nombre y notas de cada estudiante
for i in range(Nc): 
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    nombres_estudiantes.append(nombre)
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} del estudiante {nombre}: "))
        notas.append(nota)
    notas_estudiantes.append(notas)

# Calcular y mostrar el promedio de cada estudiante
for i in range(Nc):
    promedio = sum(notas_estudiantes[i]) / 3
    print(f"El promedio del estudiante {nombres_estudiantes[i]} es: {promedio}")

# Calcular y mostrar el promedio general del curso
promedio_general = sum([sum(notas) for notas in notas_estudiantes]) / (Nc * 3)
print(f"El promedio general del curso es: {promedio_general}")