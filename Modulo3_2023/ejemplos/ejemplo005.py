# VERSION 2
# Podemos enviar como parametro de una funcion otra funcion
import time

"""
En cada funcion se repite el metodo time.sleep(4). En este ejemplo es solo una linea de codgigo la que se repite
. Pero en una aplicaion podemos tener muchas mas
"""
"""
La forma mas basica para construir una funcion decoradora
def retardar_ejecucion(funcion):
    def funcion_anidada():
        funcion()
    return funcion_anidada

"""

def retardar_ejecucion(funcion):
    def funcion_anidada():
        # Puedo ejecutar codigo antes de la llamada a la funcion
        time.sleep(4.0)
        funcion()
        # Puedo ejecutar codigo despues de la llamada a la funcion
    return funcion_anidada

def saludar():
    print("Saludo despues de 4 segundos")

retardar_saludar = retardar_ejecucion(saludar)
retardar_saludar()

def despedirse():
    print("Despedirse despues de 4")

retardar_despedirse = retardar_ejecucion(despedirse)
retardar_despedirse()

def conocerce():
    print("Mucho gusto despues de 4 segundos")

retardar_conocerse = retardar_ejecucion(conocerce)
retardar_conocerse()
