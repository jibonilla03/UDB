# VERSION 1
import time

"""
En cada funcion se repite el metodo time.sleep(4). En este ejemplo es solo una linea de codgigo la que se repite
. Pero en una aplicaion podemos tener muchas mas
"""


def saludar():
    time.sleep(4.0)
    print("Saludo despues de 4 segundos")

def despedirse():
    time.sleep(4.0)
    print("Despedirse despues de 4")

def conocerce():
    time.sleep(4.0)
    print("Mucho gusto despues de 4 segundos")


saludar()
despedirse()
conocerce()