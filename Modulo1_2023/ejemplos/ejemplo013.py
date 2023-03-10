import ejemplo013Test
import random
print(ejemplo013Test.nombre)

# Generar aleatorios enteros
aleatorio_entero = random.randint(1, 100) # Genera valores enteros entre 1 y 100
print(aleatorio_entero)

# Generar aleatorios flotantes
aleatorio_float = random.random() # valores entre 0 y  1
print(round(aleatorio_float,2))


aleatorio_menor_5 = aleatorio_float * 5
print(aleatorio_menor_5)
