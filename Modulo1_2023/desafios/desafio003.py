

print("CLASIFICACION DE LA OMS DEL ESTADO NUTRICIONAL DE ACUERDO CON EL IMC")
print("CALCULO DE IMC DE UNA PERSONA:")
estatura = float(input("Digite su estatura en metros:   \n"))
peso = float(input("Digite su peso en kilogramos:   \n"))
estatura2 = float((estatura ** 2))
IMC = peso / estatura2    
print(f"Estatura = {estatura}")
print(f"Peso = {peso} \n")
if IMC <= 18.5:
    clasificacion = "Peso bajo"        
    if IMC < 16:
        print(f"Entras en la clasificación de {clasificacion}, tu IMC es de {IMC}, considerado como 'Severa'")
    elif 16 <= IMC < 16.99:
        print(f"Entras en la clasificación de {clasificacion}, tu IMC es de {IMC}, considerado como 'Moderada'")
    else:
        print(f"Entras en la clasificación de {clasificacion}, tu IMC es de {IMC}, considerado como 'Leve'")
elif 18.5 <= IMC < 24.99:
    clasificacion = "Normal"        
    print(f"Entras en la clasificación {clasificacion}, tu IMC es de {IMC}, 'F E L I C I D A D E S . . . ! ! !'")
elif 25 <= IMC <= 30:
    clasificacion = "Preobesidad"        
    print(f"Entras en la clasificación de {clasificacion}, tu IMC es {IMC}, 'A cuidar esa dieta...!!!'")
elif IMC >= 30:
    clasificacion = "Obesidad"        
    if 30 <= IMC <= 34.99:
        print(f"Entras en la clasificación de {clasificacion}, tu IMC es {IMC}, específicamente como 'Leve'")
    elif 35 <= IMC <= 39.99:
        print(f"Entras en la clasificación de {clasificacion}, tu IMC es {IMC}, específicamente como 'Media'")
    else: 
        print(f"Entras en la clasificación de {clasificacion}, tu IMC es {IMC}")