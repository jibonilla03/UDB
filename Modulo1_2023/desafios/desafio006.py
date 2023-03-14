# Desafío 6. Calcular la posibilidad de pasar el diplomado. 14
# Para resolver este ejercicio deberás calcular la posibilidad que tiene una persona de pasar el curso, para
# ello aprenderás a utilizar dos funciones más:

nombres = input("Ingrese sus nombres \n")
apellidos = input("Ingrese sus apellidos \n")

nombres = nombres.lower()
apellidos = apellidos.lower()

p = nombres.count("p")
a1 = nombres.count("a")
s = nombres.count("s")
a2 = nombres.count("a")
r = nombres.count("r")

suma_nombre = p + a1 + s + a2 + r

d = apellidos.count("d")
i = apellidos.count("i")
e = apellidos.count("e")
z = apellidos.count("z")

suma_apellido = d + i + e + z 

resultado = str(suma_nombre) + str(suma_apellido)

if int(resultado) < 20:
    print(f"Tu porcentaje es {resultado}% está difícil la situación")
elif 20 <= int(resultado) <= 60:
    print(f"Tu porcentaje es {resultado}% tu puedes lograrlo, debes esforzarte")
else:
    print(f"Tu porcentaje es {resultado}% estás cerca de tu meta")