#from cafe import Cafe

class Maquina_Expendedora:
    # Agregar atributo estado
    def __init__(self):
        self.recursos = {
            "agua": 300,
            "leche": 200,
            "cafe": 100
        }

    def imprimir_reporte(self):
        print(f"Agua: {self.recursos['agua']} ml")
        print(f"Leche: {self.recursos['leche']} ml")
        print(f"Cafe: {self.recursos['cafe']} gr")

    # Agregar recursos a maquina expendedora

    def hay_suficientes_recursos(self, obj_cafe):
        suficiente = True
        for ingrediente in obj_cafe.ingredientes:
            if obj_cafe.ingredientes[ingrediente] > self.recursos[ingrediente]:
                print(f"Lo sentimos no tenemos suficiente {ingrediente}")
                suficiente = False
        return suficiente
    
    def hacer_cafe(self, obj_cafe):
        for ingrediente in obj_cafe.ingredientes:
            self.recursos[ingrediente] -= obj_cafe.ingredientes[ingrediente]
        print(f"Su cafe {obj_cafe.nombre} esta listo !!!")

"""
maquina_expendedora = Maquina_Expendedora()
print(maquina_expendedora.recursos)
maquina_expendedora.imprimir_reporte()
# En la maquina: 300 200 100
maquina_expendedora = Maquina_Expendedora()
cafe_latte = Cafe("Latte", 100, 100, 25, 2)
print(maquina_expendedora.hay_suficientes_recursos(cafe_latte)) # True

"""




