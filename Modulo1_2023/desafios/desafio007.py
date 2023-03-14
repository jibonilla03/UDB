# Desafío 7. Generar aleatorios 15
# Crear una solución que simule el lanzamiento de una moneda que indique si el resultado es cara o corona.
# La salida en pantalla indicará el resultado
import random
moneda = random.randint(0, 1)
if moneda == 0:
    print("Cara")
else:
    print("Corona")

