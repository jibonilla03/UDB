class VerificarPreguntas:
    def __init__(self, lista_preguntas):
        self.lista_preguntas = lista_preguntas
        self.numero_pregunta = 0
        
    def mostrar_pregunta(self, numero_pregunta=0):
        respuesta = input(f"{numero_pregunta}: {self.lista_preguntas[numero_pregunta+1].texto} (True/False)?")
        return respuesta
    
    def aun_hay_preguntas(self, numero_pregunta):
        if numero_pregunta == len(self.lista_preguntas):
            return False
        return True