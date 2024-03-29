# ingresamos el nombre del usuario #
usuario = str(input("indique su nombre: "))

# ingresamos los consumos diarios #
Dia1 = float(input("comida consumida del dia 1 de su familia:  "))
Dia2 = float(input("comida consumida del dia 2 de su familia:  "))
Dia3 = float(input("comida consumida del dia 3 de su familia:  "))

# Calcular el promedio de consumos #
promedio =  (Dia1 + Dia2 + Dia3)/3

# Mostramos el msj por pantalla #
print ("Estimado/a " + str(usuario) + " Su promedio es: " + str(promedio) + " del consumo de su familia del dia.")
