# Script para registrar y mostrar datos personales de una persona.
# Solicita nombre, apellido, año de nacimiento y ciudad, y calcula la edad.

nombre = str(input("Nombres: "))
apellido = str(input("Apellidos: "))
año_nacimiento = int(input("Año de nacimiento: "))
ciudad = str(input("Ciudad: "))

edad = 2024 - año_nacimiento  # Cálculo de edad

print(f"Nombre Completo: {nombre} {apellido}")
print(f"Edad: ({edad})")
print(f"Ciudad: {ciudad}")