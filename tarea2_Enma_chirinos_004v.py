import random  # Importamos la librería random para generar números aleatorios

print("Bienvenido al juego de adivinanza.")  # Mensaje de bienvenida

# Solicitar límites del rango
while True:
    try:
        # Pedimos al usuario que ingrese el límite inferior
        limite_inferior = int(input("Ingrese límite inferior: "))
        # Pedimos al usuario que ingrese el límite superior
        limite_superior = int(input("Ingrese límite superior: "))
        # Verificamos que el límite inferior sea menor que el superior
        if limite_inferior < limite_superior:
            break  # Si la condición se cumple, salimos del bucle
        else:
            print("El límite inferior debe ser menor que el límite superior. Intente de nuevo.")
    except ValueError:
        # Si el usuario ingresa un valor no válido, mostramos un mensaje de error
        print("Por favor, ingrese números enteros válidos.")

# Calcular el punto medio y el ajuste
punto_medio = (limite_inferior + limite_superior) / 2  # Calculamos el punto medio del rango
ajuste = (limite_superior - limite_inferior) * 0.2  # Calculamos el 20% del rango total

# Generar el número aleatorio
# Generamos un número aleatorio sumando o restando el ajuste al punto medio
numero_secreto = random.uniform(punto_medio - ajuste, punto_medio + ajuste)
numero_secreto = round(numero_secreto)  # Redondeamos el número para trabajar con enteros

intentos = 3  # Número máximo de intentos permitidos
intentos_previos = []  # Lista para almacenar los intentos del usuario

# Bucle para los intentos del usuario
for intento in range(1, intentos + 1):
    try:
        # Pedimos al usuario que adivine el número
        adivinanza = int(input(f"Intente adivinar (Intento {intento}/{intentos}): "))
        intentos_previos.append(adivinanza)  # Guardamos el intento en la lista
        
        if adivinanza == numero_secreto:
            # Si el usuario adivina correctamente, mostramos un mensaje de felicitación
            if intento == 1:
                print("Felicitaciones, adivinó en el primer intento.")
            elif intento == 2:
                print("Felicitaciones, adivinó en su segundo intento.")
            else:
                print("Felicitaciones, adivinó en su último intento.")
            break  # Salimos del bucle porque el usuario ganó
        elif intento < intentos:
            # Si el intento no es el último, damos una pista
            if adivinanza < numero_secreto:
                print("El número es mayor.")  # Indicamos que el número secreto es mayor
            else:
                print("El número es menor.")  # Indicamos que el número secreto es menor
            
            if intento == 2:
                # En el segundo intento, proporcionamos una pista adicional
                distancia_1 = abs(intentos_previos[0] - numero_secreto)  # Distancia del primer intento
                distancia_2 = abs(intentos_previos[1] - numero_secreto)  # Distancia del segundo intento
                if distancia_1 < distancia_2:
                    # Si el primer intento está más cerca, lo indicamos
                    print("Te daré una pista:")
                    print(f"El número que buscas está más cerca de {intentos_previos[0]} que de {intentos_previos[1]}")
                else:
                    # Si el segundo intento está más cerca, lo indicamos
                    print("Te daré una pista:")
                    print(f"El número que buscas está más cerca de {intentos_previos[1]} que de {intentos_previos[0]}")
        else:
            # Si el usuario no adivina en el último intento, pierde
            print("Perdiste.")
            print(f"El número era: {numero_secreto}")  # Mostramos el número secreto
    except ValueError:
        # Si el usuario ingresa un valor no válido, mostramos un mensaje de error
        print("Por favor, ingrese un número entero válido.")