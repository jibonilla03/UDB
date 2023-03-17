import random
nombres = input("Escriba los nombres de los integrantes separados por una coma ")
print(nombres)
lista_nombres = nombres.split(",")
# La función split de un string separa cada string encontrado hasta la coma
# y los agrega a una lista
# Quite el comentario de la siguiente línea para comprobarlo:
print(lista_nombres)
# Ahora que ya tiene el string como una lista de string seleccione
# aleatoriamente el compañero que explicará la solución
# Escriba su código abajo de ésta línea
longitud = len(lista_nombres) - 1
num_aleatorio = random.randint(0, longitud)
print("Numero aleatorio es", num_aleatorio)
print(lista_nombres[num_aleatorio])

#"Jimmy,Jose,Erika,Pedro,Fatima" "Jimmy","Jose","Erika","Pedro","Fatima"

#FranciscoFernandez,GeovanyMejia,CarlosDescamps,JimmyBonilla