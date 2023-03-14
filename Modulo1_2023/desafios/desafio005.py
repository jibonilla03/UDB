# Desafío 5. Calcular el total a pagar por una hamburguesa. If anidados, elif 13
# Calcular el total a cancelar por una hamburguesa de acuerdo al siguiente menú:
# 1. BigMac $ 7
# 2. CheeseBurguer $ 6
# 3. QuarterPounder $ 5
# Después que se haya seleccionado la hamburguesa, preguntar se desea agregar queso extra, lo cual
# tiene un precio extra de $1

bigmac = 7
cheese_burger = 6
quarter_burger = 5
print("MENU")
print("1. BigMac ", bigmac)
print("2. CheeseBurguer ", cheese_burger)
print("3. QuarterPounder ", quarter_burger)
hamburguesa = int(input("Cual es la hamburguesa que desea pedir? 1, 2, 3 "))
queso_extra = input("Desea agregar queso extra por $1? S/N")
if queso_extra.upper() == "S":
    if hamburguesa == 1:
        total = bigmac + 1
    elif hamburguesa == 2:
        total = cheese_burger + 1
    elif hamburguesa == 3:
        total = quarter_burger + 1
else:
    if hamburguesa == 1:
        total = bigmac
    elif hamburguesa == 2:
        total = cheese_burger
    elif hamburguesa == 3:
        total = quarter_burger

print("El total a cancelar es: ", total)