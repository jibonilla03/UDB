# Diccionarios

significado_color = {
    "verde" : "diplomacia, negociacion",
    "azul" : "fuerza",
    "amarillo" : "habilidades de combate",
}

# Obtener un valor de un diccionario:
print(significado_color["amarillo"])

# Agregar un elemento al diccionario
significado_color["purpura"] = "Valor"

print(significado_color)


# Crear un diccionario vacio
diccionario_vacio = {}

# Borrar elementos del diccionario
# significado_color = {}

# Modificar un elemento
significado_color["purpura"] = "Nuevo elemento"

# Recorrer el diccionario
for significado in significado_color:
    print(significado) # Esto imprime las keys o indices
    print(significado_color[significado]) # Imprime el valor de cada key en el diccionario