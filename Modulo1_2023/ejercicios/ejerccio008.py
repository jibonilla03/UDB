esperanza_vida_hombre = 66
esperanza_vida_mujer = 75


genero = input("Cual es su genero? H - hombre, M - mujer ")
edad = int(input("Cual es tu edad? "))

if genero == "H" :
    resultado = esperanza_vida_hombre - edad
else:
    resultado = esperanza_vida_mujer - edad

resultado_meses = resultado * 12
resultado_semana = resultado * 52
resultado_dias = resultado * 365
print(f"Tienes {resultado} años, {resultado_meses} meses, {resultado_semana} semanas y {resultado_dias} para vivir en El Salvador")


