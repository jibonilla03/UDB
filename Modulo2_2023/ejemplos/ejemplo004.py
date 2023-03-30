class Factura:

    #vendedor = "Juan Antonio"

    def __init__(self, codigo_factura, vendedor):
        self.codigo_factura = codigo_factura
        self.vendedor = vendedor
        self.lista_productos = []

    # Este metodo se encarga de tomar el producto por parametro y lo
    # agrega a la lista, utilizando el metodo append
    def agregar_producto(self, producto):
        self.lista_productos.append(producto)