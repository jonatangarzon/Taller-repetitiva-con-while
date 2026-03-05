password_correcta = "python123"
password = ""

while password != password_correcta:
    password = input("Introduce la contraseña: ")
    
    if password != password_correcta:
        print("Error")

print("Acceso concedido")