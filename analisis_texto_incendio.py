# Script para analizar un texto breve sobre un incendio.
# Calcula la cantidad de caracteres, muestra la primera letra, el texto en mayúsculas/minúsculas,
# y cuenta cuántas veces aparece la palabra "miedo".

text = str(input("Indique de forma breve lo sucedido del incendio ocasionado: "))

cantidad_caracteres = len(text)  # Número de caracteres
primera_letra = text[0] if text else ''  # Primera letra, si hay texto

print("Números de caracteres:", cantidad_caracteres)
print("Primera letra es:", primera_letra)
print("Texto en mayúsculas:", text.upper())
print("Texto en minúsculas:", text.lower())
print("Cantidad de veces que aparece 'miedo':", text.count("miedo"))