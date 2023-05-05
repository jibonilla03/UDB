import time


def calcular_velocidad_ejecucion(funcion):
    def funcion_anidada():
        global tiempo_transcurrido
        before_time = time.time()
        funcion()
        after_time = time.time()
        tiempo_transcurrido = (after_time - before_time)
    return funcion_anidada

@calcular_velocidad_ejecucion
def funcion_rapida():
    for i in range(10_000):
        i * i

@calcular_velocidad_ejecucion
def funcion_lenta():
    for i in range(10_000_000):
        i * i


print(f"Tiempo de ejecucion de {funcion_rapida.__name__}  es", tiempo_transcurrido)
print(f"Tiempo de ejecucion de {funcion_lenta.__name__}  es", tiempo_transcurrido)


