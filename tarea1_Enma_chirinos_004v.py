# Valores base
ARANCEL_BASE = 2200000  # Valor base del arancel
MATRICULA_BASE = 95000  # Valor base de la matrícula

# Mensaje de bienvenida
print("Bienvenido al sistema de cálculo de beneficios para estudiantes de primer año.")

# Lista para almacenar los datos de los estudiantes
estudiantes = []

# Bucle principal para ingresar datos de estudiantes
while True:
    # Solicitar datos del estudiante
    print("\nIngrese los datos del estudiante:")
    nombre = input("Nombre: ")  # Nombre del estudiante
    rut = input("RUT: ")  # RUT del estudiante

    # Validar promedio
    while True:
        try:
            promedio = float(input("Ingrese su promedio (0.0 - 7.0): "))  # Solicitar promedio
            if 0.0 <= promedio <= 7.0:  # Verificar que esté en el rango permitido
                if promedio >= 3.95:  # Verificar que sea suficiente para aprobar
                    promedio = round(promedio, 2)  # Redondear a 2 decimales
                    break  # Salir del bucle si es válido
                else:
                    print("El promedio debe ser igual o mayor a 3.95 para aprobar.")
            else:
                print("El promedio debe estar entre 0.0 y 7.0.")
        except ValueError:
            print("Por favor, ingrese un número válido.")  # Manejar errores de entrada

    # Validar decil
    while True:
        try:
            decil = int(input("Ingrese el decil (1-10): "))  # Solicitar decil
            if 1 <= decil <= 10:  # Verificar que esté en el rango permitido
                break  # Salir del bucle si es válido
            else:
                print("El decil debe estar entre 1 y 10.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")  # Manejar errores de entrada

    # Calcular descuentos en el arancel
    if promedio > 6.5:  # Si el promedio es mayor a 6.5
        if decil in [1, 2]:  # Deciles 1 y 2
            descuento_arancel = 0.25  # 25% de descuento
        elif decil in [3, 4]:  # Deciles 3 y 4
            descuento_arancel = 0.18  # 18% de descuento
        else:  # Otros deciles
            descuento_arancel = 0  # Sin descuento
    elif 5.5 < promedio <= 6.5:  # Si el promedio está entre 5.5 y 6.5
        if decil in [1, 2]:  # Deciles 1 y 2
            descuento_arancel = 0.15  # 15% de descuento
        elif decil in [3, 4]:  # Deciles 3 y 4
            descuento_arancel = 0.12  # 12% de descuento
        else:  # Otros deciles
            descuento_arancel = 0  # Sin descuento
    else:  # Si el promedio es menor o igual a 5.5
        descuento_arancel = 0  # Sin descuento

    # Calcular descuentos en la matrícula
    descuento_matricula = 0.12 if decil in [1, 2, 3] else 0  # 12% para deciles 1, 2 y 3
    if promedio >= 6.0 and decil in [1, 2, 3]:  # Si el promedio es mayor o igual a 6.0
        descuento_matricula += 0.05  # 5% adicional

    # Calcular valores finales
    arancel_final = ARANCEL_BASE * (1 - descuento_arancel)  # Aplicar descuento al arancel
    matricula_final = MATRICULA_BASE * (1 - descuento_matricula)  # Aplicar descuento a la matrícula

    # Guardar datos del estudiante en la lista
    estudiantes.append({
        "nombre": nombre,
        "rut": rut,
        "promedio": promedio,
        "decil": decil,
        "arancel_final": arancel_final,
        "matricula_final": matricula_final,
        "descuento_arancel": descuento_arancel > 0 or descuento_matricula > 0  # Indica si tiene algún descuento
    })

    # Mostrar resultados del cálculo
    print(f"\nResultados:")
    print(f"Estudiante: {nombre}")
    print(f"RUT: {rut}")
    print(f"Promedio: {promedio}")
    print(f"El valor del arancel es: {arancel_final:,.0f} pesos.")  # Formato con separador de miles
    print(f"El valor de la matrícula es: {matricula_final:,.0f} pesos.")  # Formato con separador de miles

    # Preguntar si desea ingresar otro estudiante
    continuar = input("\n¿Desea ingresar otro estudiante? (s/n): ").strip().lower()
    if continuar != 's':  # Si no responde "s", salir del bucle
        break

# Mostrar lista de estudiantes ingresados al final
print("\nLista de estudiantes ingresados:")
total_con_descuento = 0  # Contador de estudiantes con descuento
for estudiante in estudiantes:
    print(f"{estudiante['nombre']} - RUT: {estudiante['rut']} - Promedio: {estudiante['promedio']} - "
          f"Arancel: {estudiante['arancel_final']:,.0f} - Matrícula: {estudiante['matricula_final']:,.0f}")
    if estudiante["descuento_arancel"]:  # Si tiene algún descuento
        total_con_descuento += 1

# Mostrar resumen final
print("\nResumen final:")
print(f"Total de estudiantes ingresados: {len(estudiantes)}")  # Total de estudiantes
print(f"Total de estudiantes con algún descuento: {total_con_descuento}")  # Total con descuentoen
print("Gracias por usar el sistema de cálculo de beneficios. ¡Hasta luego!")  # Mensaje de despedida
# Fin del programa