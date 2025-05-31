# main.py
# Ejemplo de uso de funciones, condicionales y ciclos en Python.
# NOTA: Este ejemplo depende de un módulo externo llamado 'funcionesmateriales' que debe tener una función resistenciaMaterial(x, y).

import funcionesmateriales

def resistencia_material(x, y):
    """
    Demuestra condicionales, ciclos y cómo llamar una función externa.
    """
    # Condicional simple
    if x > y:
        print("ojo")
    else:
        print("cara")
    
    # Ciclo for sobre los valores x e y
    for i in [x, y]:
        if x < i:
            print("hola")
        else:
            print("chao")
    
    # Ciclo while para mostrar un mensaje mientras x < y
    temp_x = x
    while temp_x < y:
        print("Locura", temp_x)
        temp_x += 1
    
    # Ejemplo de operación matemática compleja
    z = (x**2 + y**2)**2 + (x**2 - y**2)
    print("Resultado operación matemática:", z)
    
    # Llamada a función externa (supuesto)
    resultado = funcionesmateriales.resistenciaMaterial(x, y)
    print("Resultado función externa:", resultado)
    return resultado

# Ejecución de la función principal
resistencia_material(2, 20)