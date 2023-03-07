# Desafio 6: Type, input, conversion de tipos de datos
# Solicitar al usuario un numero de dos digitos y hacer la suma de cada uno de los digitos. Por ejemplo"
# - Si el usuario digita 48 la respuesta sera 4+8=12
# - Si el usuario digita 46 la respuesta sera 5+6=11

print("Ingrese un numero de dos digitos")
numero=input()
suma=int(numero[0])+int(numero[1])
print("Total:{}".format(suma))