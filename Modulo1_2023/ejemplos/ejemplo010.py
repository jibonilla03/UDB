# Condicionales: If anidado
edad = int(input("Digite su edad "))
if edad >= 18:
    print("Felicidades ya puedes obtener la licencia")
    licencia_pesada = int(input("La licencia solicitada es pesada 1.SI 2.NO "))
    if licencia_pesada == 1:
        print("El costo por el tramite es de $100")
    elif licencia_pesada == 2:
        print("El costo por el tramite es de $50")
    else:
        print("Seleccion no valida")
else:
    print("Aun no puedes tramitar tu licencia")
