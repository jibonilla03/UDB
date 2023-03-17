import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
caracteres = ['*', '_', '-', '$', '%', '/', '(', ')', '=', '[', ']', '+']

longitud_password = int(input("¿Longitud de la contraseña generada? "))
cantidad_numeros = int(input("Cantidad de numeros: "))
cantidad_caracteres = int(input("Cantidad de caracteres especiales: "))
cantidad_letras = longitud_password - cantidad_caracteres - cantidad_numeros



letras_elegidas = []
for letra in range(0,cantidad_letras):
    letras_elegidas.append(random.choice(letras))

print(letras_elegidas)

numeros_elegidos = []
for letra in range(0,cantidad_numeros):
    numeros_elegidos.append(random.choice(numeros))

print(numeros_elegidos)

caracteres_elegidos = []
for letra in range(0,cantidad_caracteres):
    caracteres_elegidos.append(random.choice(caracteres))

print(caracteres_elegidos)

letras_elegidas.extend(numeros_elegidos)
letras_elegidas.extend(caracteres_elegidos)
print(letras_elegidas)

random.shuffle(letras_elegidas)

print(letras_elegidas)

print(''.join(letras_elegidas))







   



