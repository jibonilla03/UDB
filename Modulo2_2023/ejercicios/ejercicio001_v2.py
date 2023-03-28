import random
opciones = {
"piedra" : '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''' ,

"papel" : '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',

"tijera" : '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
}

################################### FUNCIONES ###############################################
def jugar(opcion_usuario, opcion_pc):
    if opcion_usuario == opcion_pc:
        return "EMPATE"
    elif opcion_usuario == "piedra" and opcion_pc == "tijera":
        return "GANASTE"
    elif opcion_usuario == "papel" and opcion_pc == "piedra":
        return "GANASTE"
    elif opcion_usuario == "tijera" and opcion_pc == "papel":
        return "GANASTE"
    else:
        return "PERDISTE"
    
def imprimir_seleccion(opcion, jugador):
    if jugador == 0:
        usuario = "Usuario"
    elif jugador == 1:
        usuario = "Computadora"
    else:
        print("Jugador no valido")

    print(f"{usuario} selecciona", opcion)
    print(opciones[opcion])

################################### MAIN ###############################################
print("Bienvenido al juego de piedra, papel o tijera")
seleccion_usuario = int(input("Seleccione una opcion 1.Piedra, 2.Papel, 3.Tijera: "))

match seleccion_usuario:
    case 1:
        opcion_usuario = "piedra"

    case 2:
        opcion_usuario = "papel"

    case 3:
        opcion_usuario = "tijera"
    case _:
        print("Opcion no valida, Seleccione una opcion 1.Piedra, 2.Papel, 3.Tijera: ")


imprimir_seleccion(opcion_usuario, 0)

opcion_pc = random.choice(list(opciones.keys()))

imprimir_seleccion(opcion_pc, 1)

print(jugar(opcion_usuario, opcion_pc))





    


