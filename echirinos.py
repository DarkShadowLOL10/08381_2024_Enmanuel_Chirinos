# echirinos.py
# Ejemplo simple de comparación entre una distancia ingresada y un máximo permitido.

DMAX = 100
msg = "hola mundo"
print(msg)

zona1 = float(input("Distancia de la zona 1: "))

# Comparación correcta usando el valor numérico ingresado
if zona1 > DMAX:
    print("Muy lejos")
else:
    print("Muy cerca")