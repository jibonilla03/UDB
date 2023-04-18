class Maquina_Dinero:
    MONEDA = "$"
    VALORES_MONEDAS = {
        "un dolar": 1,
        "veintecinco": 0.25,
        "diez": 0.10,
        "cinco": 0.05
    }

    def __init__(self):
        self.ingreso_por_ventas = 0
        self.dinero_recibido = 0

    def reporte(self):
        print(f"Ventas {self.MONEDA}{self.ingreso_por_ventas}")

    def procesar_dinero(self):
        self.dinero_recibido = 0
        print("Por favor ingrese las monedas: ")
        for moneda in self.VALORES_MONEDAS:
            self.dinero_recibido += int(input(f"Cuantas monedas de {moneda} ")) * self.VALORES_MONEDAS[moneda]
        return round(self.dinero_recibido, 2)
    
    # Verificar si el dinero ingresado > costo_cafe
    # Calcular el cambio

    def procesar_pago(self, costo_cafe):
        self.procesar_dinero()
        if self.dinero_recibido >= costo_cafe:
            cambio = round(self.dinero_recibido - costo_cafe, 2)
            print(f"Aqui esta su cambio: {self.MONEDA}{cambio}")
            self.ingreso_por_ventas += costo_cafe
            return True
        else:
            print(f"Lo siento, el dinero ingresado: {self.dinero_recibido} no es suficiente!!!")
            print("El dinero ingresado fue devuelto")
            return False
        


"""
maquina = Maquina_Dinero()
# maquina.procesar_dinero()
print(maquina.procesar_pago(2.5))
"""
