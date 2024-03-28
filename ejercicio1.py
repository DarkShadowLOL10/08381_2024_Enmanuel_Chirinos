usuario = str(input("indique su nombre: "))

dia_consumo1 = float(input("comida consumida del dia 1 de su familia:  "))
dia_consumo2 = float(input("comida consumida del dia 2 de su familia:  "))
dia_consumo3 = float(input("comida consumida del dia 3 de su familia:  "))

promedio_del_consumo =  (dia_consumo1 + dia_consumo2 + dia_consumo3)/3

print ("Estimado/a " + usuario+ " Su promedio es: " + str(promedio_del_consumo) + " del consumo de su familia del dia.")