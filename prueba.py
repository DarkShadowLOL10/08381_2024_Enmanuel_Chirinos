nombres_estudiantes = [] 
notas_estudiantes = []

Nc = int(input("ingrese el n° de estudiantes: ")) 

for i in range(Nc): 
    nombre = input("ingrese el nombre del estudiante: ")
    nombres_estudiantes.append(nombre)

    notas= []
    for j in range(3):
        nota = float(input(f"ingrese su nota: {j+1} del estudiante: {nombre}: "))
        notas.append(nota)
    
    notas_estudiantes.append(notas)

for i in range(Nc): #calcula el promedio de cada estudiante #
    promedio = sum(notas_estudiantes[i]) / 3
    print(f"El promedio del estudiante {nombres_estudiantes[i]} es: {promedio}")

promedio_general = sum([sum(notas) for notas in notas_estudiantes]) / (Nc * 3)
print(f"El promedio general del curso es: {promedio_general}")

# Aplica el limite del porcentaje de la nota final... #
#lo cual no sobrepasa el 100% #
#if notas_estudiantes > 7.0:    
#notas_estudiantes = 7.0
# else: es para el caso contrario #