# Condicionales: If anidado
edad = int(input("Digite su edad "))
if edad >= 18:
    print("Felicidades ya puedes obtener la licencia")
    licencia = int(input("La licencia solicitada es pesada 1.Pesada 2.Particular 3.Liviana "))
    if licencia == 1:
        print("El costo por el tramite es de $100")
    elif licencia == 2:
        print("El costo por el tramite es de $50")
    elif licencia == 3:
        print("El costo por el tramite es de $75")
    else:
        print("Por favor elija 1, 2 o 3")
else:
    print("Aun no puedes tramitar tu licencia")