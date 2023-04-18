from pregunta import Pregunta
from datos import datos
from cuestionario import VerificarPreguntas

banco_preguntas = []

for dato in datos:
    pregunta = Pregunta(dato.get('texto'), dato.get('respuesta'))
    banco_preguntas.append(pregunta)

verificar_pregunta = VerificarPreguntas(banco_preguntas)
respuesta = verificar_pregunta.mostrar_pregunta()
print(respuesta)