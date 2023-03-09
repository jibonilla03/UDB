# Redondeo de numeros
print(round(5.6666, 2))

# Division entera
print(8 // 3) # 2

# Incremento y decremento
goles = 1
goles = goles + 2 
goles += 2 # Lineas 9 y 10  son equivalentes
goles -=1  #==> goles = goles - 1
goles *= 3 
goles /= 2
goles **=3
print(goles)

# F-strings
edad = 16
soltero = True
estatura = 1.68
print("Tu edad es: " + str(edad) + ", tu estatura es: " + str(estatura) + ", eres soltero: " + str(soltero))
# Otra opcion para imprimir el mensaje anterior
print(f"Tu edad es: {edad}, tu estatura es: {estatura}, eres soltero: {soltero}")
print("Tu edad es: {}, tu estatura es: {}, eres soltero: {}".format(edad, estatura, soltero))