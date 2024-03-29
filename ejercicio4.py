nombre = str(input("Nombres: "))
apellido = str(input("Apellidos: "))
año_nacimiento = int(input("año de nacimiento: "))
ciudad = str(input("Ciudad: "))

edad = str(2024 - (año_nacimiento))

print ("Nombre Completo: " + (nombre) ,"" + (apellido))
print ("Edad: (" + str(edad) + ")")
print ("ciudad: " + str(ciudad))