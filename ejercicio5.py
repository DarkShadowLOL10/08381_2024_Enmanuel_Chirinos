text= str(input("Indique de forma breve lo sucedido del incendio ocasionado: "))
# Cantidad de caracteres con espacio #
cantidad_caracteres = (len(text))
primera_letra = text[0]

print ("numeros_caracteres: " , cantidad_caracteres)
print ("primera letra es: " + primera_letra)
print (text.upper())
print ((text.lower()))
print (str (text.count("miedo")))