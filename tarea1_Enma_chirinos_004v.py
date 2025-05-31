# tarea1_Enma_chirinos_004v.py
# Calculadora de descuentos de arancel y matrícula para estudiantes de primer año según promedio y decil.
# Solicita datos y valida la entrada, mostrando los descuentos aplicados.

ARANCEL_BASE = 2_200_000  # Valor base del arancel
MATRICULA_BASE = 95_000   # Valor base de la matrícula

print("Bienvenido al sistema de cálculo de beneficios para estudiantes de primer año.")

estudiantes = []

while True:
    print("\nIngrese los datos del estudiante:")
    nombre = input("Nombre: ")
    rut = input("RUT: ")

    # Validación de promedio
    while True:
        try:
            promedio = float(input("Ingrese su promedio (0.0 - 7.0): "))
            if 0.0 <= promedio <= 7.0:
                if promedio >= 3.95:
                    promedio = round(promedio, 2)
                    break
                else:
                    print("El promedio debe ser igual o mayor a 3.95 para aprobar.")
            else:
                print("El promedio debe estar entre 0.0 y 7.0.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    # Validación de decil
    while True:
        try:
            decil = int(input("Ingrese el decil (1-10): "))
            if 1 <= decil <= 10:
                break
            else:
                print("El decil debe estar entre 1 y 10.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    # Calcular descuentos en el arancel
    descuento_arancel = 0
    if promedio > 6.5:
        if decil in [1, 2]:
            descuento_arancel = 0.25
        elif decil in [3, 4]:
            descuento_arancel = 0.18
    elif 5.5 < promedio <= 6.5:
        if decil in [1, 2]:
            descuento_arancel = 0.15
        elif decil in [3, 4]:
            descuento_arancel = 0.12

    arancel_final = ARANCEL_BASE * (1 - descuento_arancel)
    matricula_final = MATRICULA_BASE  # Aquí podrías agregar lógica de descuentos para matrícula si aplica

    print(f"Estudiante: {nombre} | RUT: {rut}")
    print(f"Promedio: {promedio} | Decil: {decil}")
    print(f"Arancel final a pagar: {arancel_final}")
    print(f"Matrícula final a pagar: {matricula_final}")

    # Guardar datos del estudiante
    estudiantes.append({
        "nombre": nombre,
        "rut": rut,
        "promedio": promedio,
        "decil": decil,
        "arancel_final": arancel_final,
        "matricula_final": matricula_final
    })

    # Preguntar si se desea ingresar otro estudiante
    continuar = input("¿Desea ingresar otro estudiante? (s/n): ")
    if continuar.lower() != 's':
        break

print("\nResumen de estudiantes registrados:")
for est in estudiantes:
    print(est)