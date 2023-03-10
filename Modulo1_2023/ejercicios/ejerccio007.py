# Desafio 7: Operadores matematicos, precedencia de operadores, conversiones
# Crear una aplicacion que devuelva el IMC (indice de masa corporal de una persona), cuya formula es

print("CALCULO DE IMC DE UNA PERSONA:")
estatura=float(input("Digite su estatura en metros: "))
masa=float(input("Digite su peso en Kilogramos: "))

#imc=masa/(estatura*estatura)
imc=masa/pow(estatura,2)

print(round(imc/1,1))
#print(int(imc))

if imc > 30:
    print("Obesidad")
elif 24.9 < imc <= 29.9:
    print("Sobrepeso")
elif 18.5 < imc <= 24.9:
    print("Rango normal")
else:
    print("Bajo peso")