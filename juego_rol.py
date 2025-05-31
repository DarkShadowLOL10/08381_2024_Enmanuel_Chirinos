# juego_rol.py
# Juego interactivo de rol donde el usuario toma decisiones para avanzar por caminos diferentes.

def intro():
    print("¡Bienvenido al misterioso bosque!")
    print("Te encuentras en un cruce de caminos. ¿Hacia dónde quieres ir?")
    print("1. Izquierda")
    print("2. Derecha")
    print("3. Recto")

    choice = input("Elige 1, 2 o 3: ")
    if choice == "1":
        camino_izquierda()
    elif choice == "2":
        camino_derecha()
    elif choice == "3":
        camino_recto()
    else:
        print("¡Opción no válida! Inténtalo de nuevo.")
        intro()

def camino_izquierda():
    print("Sigues el camino de la izquierda y llegas a un lago.")
    print("¿Qué haces?")
    print("1. Nadar en el lago")
    print("2. Volver al cruce de caminos")
    print("3. Caminar alrededor del lago")

    choice = input("Elige 1, 2 o 3: ")
    if choice == "1":
        print("¡Oh no! Un monstruo marino te atrapa. Fin del juego.")
    elif choice == "2":
        intro()
    elif choice == "3":
        print("Encuentras un tesoro escondido alrededor del lago. ¡Has ganado el juego!")
    else:
        print("¡Opción no válida! Inténtalo de nuevo.")
        camino_izquierda()

def camino_derecha():
    print("Sigues el camino de la derecha y encuentras una cueva oscura.")
    print("¿Qué haces?")
    print("1. Entrar en la cueva")
    print("2. Volver al cruce de caminos")
    print("3. Buscar una antorcha y luego entrar en la cueva")

    choice = input("Elige 1, 2 o 3: ")
    if choice == "1":
        print("Es demasiado oscuro para ver. Te caes en un pozo y el juego termina.")
    elif choice == "2":
        intro()
    elif choice == "3":
        print("Con la luz de la antorcha, encuentras un cofre de oro en la cueva. ¡Has ganado el juego!")
    else:
        print("¡Opción no válida! Inténtalo de nuevo.")
        camino_derecha()

def camino_recto():
    print("Sigues el camino recto y te encuentras con un troll.")
    print("¿Qué haces?")
    print("1. Luchar contra el troll")
    print("2. Volver al cruce de caminos")
    print("3. Darle al troll una galleta")

    choice = input("Elige 1, 2 o 3: ")
    if choice == "1":
        print("El troll es demasiado fuerte. Fin del juego.")
    elif choice == "2":
        intro()
    elif choice == "3":
        print("El troll está feliz con la galleta y te deja pasar. Encuentras un castillo con una princesa. ¡Has ganado el juego!")
    else:
        print("¡Opción no válida! Inténtalo de nuevo.")
        camino_recto()

# Inicia el juego
intro()