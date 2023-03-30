class Factura:
    # Las variables de clases son compartidas por todos los objetos,
    # por ejemplo la variable vendedor. Todos los objetos creados
    # a partir de la clase Factura comparten la variable vendedor
    vendedor = "Juan Antonio"

    def __init__(self, codigo_factura):
        # Variable de instancia o de objeto
        # Las variables de instancia son propias de un objeto(no son compartidas)
        self.codigo_factura = codigo_factura 