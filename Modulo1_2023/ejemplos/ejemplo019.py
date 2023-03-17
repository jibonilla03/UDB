# Crear una funcion que reciba dos parametros numericos y un paramtero
# string que sera el signo de la operacion
# La funcion debera retornar el resultados de la operacion basica
# Las operaciones basicas son: sumar, restar, multiplicar y dividir

# def operaciones_basicas(num1, num2, signo):
#     print(f"el numero es: {num1}, el numero dos es: {num2}, el signo es {signo}")
#     resultado = 1000
#     return resultado

# variable_resultado = operaciones_basicas(1,2,"+")
# print(variable_resultado)


def operaciones_basicas(num1, num2, signo):
    print(f"el numero es: {num1}, el numero dos es: {num2}, el signo es {signo}")
    resultado_operacion = 0
    if signo == "+":
        resultado_operacion = num1 + num2
    elif signo == "-":
        resultado_operacion = num1 - num2
    elif signo == "*":
        resultado_operacion = num1 * num2
    elif signo == "/":
        resultado_operacion = num1 / num2
    return resultado_operacion

# variable_resultado = operaciones_basicas(1,2,"+")
# print(variable_resultado)

continuar = "SI"
while continuar.upper() == "SI":
    numero1 = int(input("Escriba el primer numero entero: "))
    numero2 = int(input("Escriba el primer numero entero: "))
    signo_operacion = input("Escriba el signo de la operacion")
    variable_resultado = operaciones_basicas(numero1, numero2, signo_operacion)
    print(f"El resultado es:  {variable_resultado}")
    continuar = input("Desea continuar? SI, NO")


