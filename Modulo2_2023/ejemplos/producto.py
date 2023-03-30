class Producto:
    def __init__(self, codProducto, nombre, precio):
        self.codProducto = codProducto
        self.nombre = nombre
        self.precio = precio
        self.descripcion = ""

tornillo = Producto(1, "tornillo", 2.5)
brocha = Producto(2, "brocha", 2.5)
brocha.descripcion = "Brocha tamaño x"