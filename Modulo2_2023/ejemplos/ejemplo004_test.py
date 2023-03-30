from ejemplo004 import Factura

factura_01 = Factura("001", "Juan Antonio")
factura_02 = Factura("002", "Karen Patricia")

factura_01.agregar_producto("acetaminofen")
factura_01.agregar_producto("ibuprofeno")
factura_02.agregar_producto("alerfin")

print(factura_01.vendedor)
print(factura_02.vendedor)

print(factura_01.codigo_factura)
print(factura_02.codigo_factura)

print(factura_01.lista_productos)
print(factura_02.lista_productos)