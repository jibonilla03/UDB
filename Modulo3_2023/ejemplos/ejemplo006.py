# VERSION 2
# Podemos enviar como parametro de una funcion otra funcion
import time



def retardar_ejecucion(funcion):
    def funcion_anidada():
        time.sleep(4.0)
        funcion()
    return funcion_anidada

@retardar_ejecucion
def saludar():
    print("Saludo despues de 4 segundos")


@retardar_ejecucion
def despedirse():
    print("Despedirse despues de 4")

@retardar_ejecucion
def conocerce():
    print("Mucho gusto despues de 4 segundos")


saludar()
despedirse()
conocerce()

