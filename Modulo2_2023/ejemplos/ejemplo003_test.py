from ejemplo003 import Factura

factura01 = Factura("001")
factura02 = Factura("001")

# Imprimimos variables clase
print(factura01.vendedor)
print(factura02.vendedor)

# Imprimimos variables de instancia, en este caso cada variable tiene un valor
# para cada objeto creado
print(factura01.codigo_factura)
print(factura02.codigo_factura)