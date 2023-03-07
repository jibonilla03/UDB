# Desafío 5: Generador de contraseña
# Para este desafío crearás un generado de contraseña para lo cual almacena en 3 variables lo que se le
# solicita al usuario para luego unirlas en una impresión en pantalla. Puedes guiarte de la imagen
# siguiente (observa que el ingreso de dato del usuario está en la siguiente línea):

print("Generador de contraseña")
num_favorito=input("Del 1 al 100 cual es tu numero favorito?\n")
animal_favorito=input("Cual es tu animal preferido?\n")
deporte_favorito=input("Cual es tu deporte preferido?\n")

print(animal_favorito,num_favorito,deporte_favorito,sep="")
print(animal_favorito+num_favorito+deporte_favorito)