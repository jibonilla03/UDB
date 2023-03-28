import random
piedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tijera = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
################################### FUNCIONES ###############################################
def jugar(opcion_usuario, opcion_pc):
    if opcion_usuario == opcion_pc:
        return "EMPATE"
    elif opcion_usuario == 1 and opcion_pc == 3:
        return "GANASTE"
    elif opcion_usuario == 2 and opcion_pc == 1:
        return "GANASTE"
    elif opcion_usuario == 3 and opcion_pc == 2:
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

    if opcion == 1:
        print(f"{usuario} selecciona", piedra)
    elif opcion == 2:
        print(f"{usuario} selecciona", papel)
    else:
        print(f"{usuario} selecciona", tijera)

################################### MAIN ###############################################
print("Bienvenido al juego de piedra, papel o tijera")
opcion_usuario = int(input("Seleccione una opcion 1.Piedra, 2.Papel, 3.Tijera: "))

imprimir_seleccion(opcion_usuario, 0)

opcion_pc = random.randint(1, 3)

imprimir_seleccion(opcion_pc, 1)

print(jugar(opcion_usuario, opcion_pc))





    


