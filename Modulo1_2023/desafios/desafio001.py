print("Calculadora de pago")
total_factura = float(input("Cuanto es el total de la factura $ "))
propina_persona = int(input("Cual es el porcentaje de propina a dar? 10, 12, 15 "))
personas = int(input("Cuantas personas pagaran? "))

pago_total = (total_factura + (total_factura  * (propina_persona/100)))/personas

print("El pago total por cada persona es: $", pago_total )