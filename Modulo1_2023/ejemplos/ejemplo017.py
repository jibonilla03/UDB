# Funciones en Python
# $100 --> "Cien dolares"
# Cuantos dias hay entre dos fechas

precio = 1000

def total_pagar():
    descuento = precio * 0.10 #100
    print(f"El descuento es: {descuento}" )
    total_a_pagar = precio - descuento # 900
    print(f"El total a pagar es: {total_a_pagar}")

total_pagar()