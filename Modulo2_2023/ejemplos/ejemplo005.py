def sumar(*args):
    resultado  = 0
    for num in args:
        if num != "hola":
            resultado += num
            #resultado = resultado  + num
    return resultado

print(sumar(100.2, 500.5, "hola")) #600
print(sumar(1, 2, 3, 4, 5, 6, 7)) #28
print(sumar(100, 200, 300)) # 600