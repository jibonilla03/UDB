# Desafio 7: Operadores matematicos, precedencia de operadores, conversiones
# Crear una aplicacion que devuelva el IMC (indice de masa corporal de una persona), cuya formula es

print("CALCULO DE IMC DE UNA PERSONA:")
estatura=float(input("Digite su estatura en metros: "))
masa=float(input("Digite su peso en Kilogramos: "))

#imc=masa/(estatura*estatura)
imc=masa/pow(estatura,2)

print(imc//1)
#print(int(imc))