import random

vida_jugador = 50
vida_jefe = 60
numero_secreto = random.randint(1, 100)

print("⚔️ ¡Comienza la batalla contra el jefe!")
print("Adivina el número del 1 al 100 para atacar al jefe.")

while True:
    intento = int(input("Adivina el número: "))

    if intento < numero_secreto:
        print("Más alto")
    elif intento > numero_secreto:
        print("Más bajo")
    else:
        daño = random.randint(10, 20)
        vida_jefe -= daño
        print("¡Correcto! Atacaste al jefe.")
        print("Daño al jefe:", daño)
        print("vida del jefe:", vida_jefe)

        numero_secreto = random.randint(1, 100)

        if vida_jefe <= 0:
            print("🏆 ¡Derrotaste al jefe!")
            break

    # Turno del jefe
    daño_jefe = random.randint(5, 15)
    vida_jugador -= daño_jefe
    print("El jefe te atacó y te quitó", vida_jefe, "de vida.")
    print("Tu vida:", vida_jugador)

    if vida_jugador <= 0:
        print("💀 Has sido derrotado.")
        break