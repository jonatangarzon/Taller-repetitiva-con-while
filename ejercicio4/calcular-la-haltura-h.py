h = float(input("ingresa la altura inicial: "))

altura = h
rebote = 0

while altura > h/5:
    altura = altura * 0.9
    rebote = rebote + 1

print("la pelota ya no supera la quinta parte en el rebote:", rebote )