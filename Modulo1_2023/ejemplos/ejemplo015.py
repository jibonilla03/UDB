# For para correr enteros
contador = 0
lista_valores = []
#5050
# En el siguiente for no se incluyer
for num in range(1,101,1):
    # contador = contador + num
    contador += num
    print(num)
    # Agregamos los valores del contador en una lista llamada lista_valores
    lista_valores.append(num)

print(contador) #5050