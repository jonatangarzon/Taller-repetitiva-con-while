c1 = float(input("capital de pedro: "))
c2 = float(input(" capital de juan: "))
c3 = float(input("capital nesesario para el negocio: "))

mes = 0 

while (c1 + c2) < c3:
    c1 = c1*1.03
    c2 = c2*1.04
    mes = mes+1 

print("puede hacer el negocio en", mes, "mes")