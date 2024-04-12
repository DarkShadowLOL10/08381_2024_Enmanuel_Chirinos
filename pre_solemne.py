# Esto define que si el usuario ingresa caractares en vez de números, el programa le pedirá que ingrese un número válido y lo devolvera #
def obtener_entrada_numerica(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número válido.")

def obtener_datos_estudiantes():
    nombre = (input("Ingrese su nombre estudiante: "))
    edad = obtener_entrada_numerica("Ingrese su edad: ")
    comuna = (input("Ingrese su comuna de residencia: "))
    conoce_conaf = (input("¿Conoce a CONAF?: "))
    veces_participacion = obtener_entrada_numerica("¿Cuantas veces ha participado en campañas de prevención?: ")
    personas_hogar = obtener_entrada_numerica("¿Cuantas personas viven en su hogar?: ")
    incendios_vividos = obtener_entrada_numerica("¿Cuantos incendios forestales ha vivido cerca de su residencia?: ")
    
    estudiantes_uah.append([nombre, edad, comuna, conoce_conaf, veces_participacion, personas_hogar, incendios_vividos])
    nivel_prepa = float(((veces_participacion * incendios_vividos) / personas_hogar))

    # return sirve para devolver los valores de la función y se puede devolver más de un valor #
    # en este caso se devuelven 3 valores, separados por comas, y finaliza la función #
    return nivel_prepa, nombre, comuna

# aqui parte el codigo #
estudiantes_uah = []
Nce = obtener_entrada_numerica("Ingrese el N° de estudiantes: ")
for i in range(Nce):
    nivel_prepa, nombre, comuna = obtener_datos_estudiantes()
    if nivel_prepa >= 1:
        print(f"Nivel de preparación de supervivencia es suficiente del estudiante: {nombre} de la comuna de: {comuna} es de: {nivel_prepa}")
    else:
        print(f"Nivel de preparación de supervivencia es grave del estudiante: {nombre} de la comuna de: {comuna} es de: {nivel_prepa}")