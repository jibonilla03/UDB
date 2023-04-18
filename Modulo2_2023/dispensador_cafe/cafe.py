class Cafe:
    def __init__(self, nombre, agua, leche, cafe, costo):
        self.nombre = nombre
        self.costo = costo 
        self.ingredientes = {
            "agua" : agua,
            "leche" : leche,
            "cafe" : leche
        }

"""
cafe_expresso = Cafe("Expresso", 150, 0, 50, 2.5)
cafe_latte = Cafe("Latte", 100, 100, 25, 2)
cafe_capuccino = Cafe("Capuccino", 125, 50, 100, 3)

print(cafe_expresso.ingredientes)
print(cafe_expresso.nombre)
print(cafe_expresso.costo)
"""