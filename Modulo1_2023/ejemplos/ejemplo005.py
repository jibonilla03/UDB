# Tipos de datos y conversiones
nombre = input("Digite su nombre: ")
longitud_del_nombre = len(nombre)
"""
Podemos conocer el tipo de dato que almacena una variable
utilizando la funcion type
"""
print(type(nombre)) # str == string
print(type("Jimmy"))
print(type(longitud_del_nombre)) # int == integer == entero
print(type(True)) # bool == booleano
print(type(False)) # bool == booleano
print(type(10.52)) # float == flotante

# Conversion de tipos de datos
longitud_del_nombre_string = str(longitud_del_nombre)
print(type(longitud_del_nombre_string))
print("La longitud del nombre es: " + longitud_del_nombre_string)
print(int(10.85)) # 10
print(bool(1)) # True
print(bool(0)) # False
print(bool(-10)) # True
print(bool(0.0)) # False
print(float(10)) # 10.0
print(bool("Hola")) # True
print(bool("")) # False