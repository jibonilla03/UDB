# AND / OR
# and se cumple si todas las condiciones son verdaderas
# or se comple si al menos una condicion es verdadera
edad = int(input("Digite su edad "))
sexo = "F"
salario = 2000
if edad <= 3:
    print("Eres un bebe")
elif edad >  3 and edad <= 10:
    print("Eres un niño")
# elif edad > 10 and edad <=18:
elif 10 < edad <= 18:
    print("Eres un adolecente")

# or
if edad == 10 or edad == 20 and salario <= 1000:
    print("Tu edad es multiplo de 10")

# not
print(not edad < 10)