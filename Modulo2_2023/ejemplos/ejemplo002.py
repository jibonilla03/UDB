class Medicamento:
    # Metodo constructor de la clase Medicamento
    # Todos los objetos creados a partir de esta clase
    # deben tener nombre_generico y descripcion porque
    # asi me lo indica el constructor
    precio = 0
    # atributo se le da ese nombre en los diagrmas y se 
    # convierte en variables en el codigo
    def __init__(self, nombre_generico, descripcion):
        self.nombre_generico = nombre_generico
        self.descripcion = descripcion

    def calcular_precio_venta(self):
        if self.precio > 10:
            return  self.precio + 5
        if self.precio > 100:
            return self.precio + 10
        print("Calcular precio de venta")