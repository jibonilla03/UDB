# Desafío 4: Comprender el funcionamiento de variables.
# Descargue del aula virtual el código para este ejercicio. Para solucionar este ejercicio deberás agregar
# líneas de código sin cambiar las que ya tiene.
# La salida en pantalla deberá ser así:

# Por favor no modifiques esta parte del código
num1 = input("Ingresa un numero entero (num1): ")
num2 = input("Ingresa otro numero entero (num2): ")
####################################
var_temporal = num1
num1 = num2
num2 = var_temporal

#num1, num2 = num2, num1
####################################
# Por favor no modifiques esta parte del código
print("num1: " + num1)
print("num2: " + num2)