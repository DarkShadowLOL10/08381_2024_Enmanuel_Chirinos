# ejercicio5.py
# Analiza un texto breve, contando caracteres, mostrando la primera letra, y buscando la palabra 'miedo'.

text = input("Indique de forma breve lo sucedido del incendio ocasionado: ")
cantidad_caracteres = len(text)
primera_letra = text[0] if text else ''

print("Número de caracteres:", cantidad_caracteres)
print("Primera letra es:", primera_letra)
print("Texto en mayúsculas:", text.upper())
print("Texto en minúsculas:", text.lower())
print("Cantidad de veces que aparece 'miedo':", text.count("miedo"))