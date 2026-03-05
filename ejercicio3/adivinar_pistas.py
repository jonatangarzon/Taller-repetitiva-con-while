import random

# La computadora elige un número entre 1 y 100
numero_secreto = random.randint(1, 100)

intento = 0

while intento != numero_secreto:
    intento = int(input("Adivina el número (1-100): "))

    if intento < numero_secreto:
        print("Más alto")
    elif intento > numero_secreto:
        print("Más bajo")
    else:
        print("¡Correcto! Adivinaste el número.")