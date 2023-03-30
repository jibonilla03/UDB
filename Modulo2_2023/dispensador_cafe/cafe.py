class Cafe:
    def __init__(self, nombre, agua, leche, cafe, costo):
        self.nombre = nombre
        self.costo = costo 
        self.ingredientes = {
            "agua" : agua,
            "leche" : leche,
            "cafe" : leche
        }

cafe_expresso = Cafe("Expresso", 150, 0, 50, 2.5)