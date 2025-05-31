# ejercicio4.py
# Solicita datos personales y calcula la edad a partir del año de nacimiento.

nombre = input("Nombres: ")
apellido = input("Apellidos: ")
año_nacimiento = int(input("Año de nacimiento: "))
ciudad = input("Ciudad: ")

edad = 2024 - año_nacimiento

print(f"Nombre Completo: {nombre} {apellido}")
print(f"Edad: {edad}")
print(f"Ciudad: {ciudad}")