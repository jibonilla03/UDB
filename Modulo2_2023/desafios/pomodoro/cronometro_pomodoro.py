from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
BLANCO = "#ffffff"
FONT_NAME = "Courier"
MINUTOS_TRABAJO = 1
MINUTOS_RECESO_CORTO = 1
MINUTOS_RECESO_LARGO = 2
num_repeticion = 0
tiempo =  None
# Definir funciones

def descontar_segundos(contador):
    contador_minutos = math.floor(contador /60)
    contador_segundos = contador % 60

    if contador_segundos < 10:
        contador_segundos = f"0{contador_segundos}"
    lbl_tiempo.config(text=f"{contador_minutos}:{contador_segundos}")
    if contador > 0:
        ventana.after(1000, descontar_segundos, contador-1)
    else:
        iniciar_cronometro()
        marca = ""
        num_session_trabajo = math.floor(num_repeticion / 2)
        for _ in range(num_session_trabajo):
            marca += "#"
        lbl_cheque.config(text=marca)

def iniciar_cronometro():
    global num_repeticion
    num_repeticion += 1

    segundos_trabajo = MINUTOS_TRABAJO * 60
    segundos_receso_corto = MINUTOS_RECESO_CORTO * 60
    segundos_receso_largo = MINUTOS_RECESO_LARGO * 60
    # Descando Largo
    if num_repeticion % 8 == 0:
        descontar_segundos(segundos_receso_largo)
        lbl_titulo.config(text="Receso", fg=RED)
    elif num_repeticion % 2 == 0:
        descontar_segundos(segundos_receso_corto)
        lbl_titulo.config(text="Receso", fg=PINK)
    else:
        descontar_segundos(segundos_trabajo)
        lbl_titulo.config(text="Trabajando", fg=GREEN)

def reiniciar_cronometro():
    ventana.after_cancel(tiempo)
    lbl_tiempo.config(text="00:00")
    lbl_titulo.config(text="Timer")
    lbl_cheque.config(text="")
    global num_repeticion
    num_repeticion = 0

# Definir ventana
ventana = Tk()
ventana.title("Pomodoro")
ventana.geometry("200x200")

# Definir etiquetas
lbl_titulo = Label(ventana, text="Cronometro Pomodoro")
lbl_titulo.grid(column=0, row=0, columnspan=2, sticky=N)

img_reloj = PhotoImage(file="./images/reloj.png").subsample(4)
lbl_reloj =Label(ventana, image=img_reloj).grid(column=0, row=1, columnspan=2)

lbl_tiempo = Label(ventana, text="00:00", bg=BLANCO)
lbl_tiempo.grid(column=0, row=1)

lbl_cheque = Label(ventana, text="")
lbl_cheque.grid(column=0, row=5)

# Definir butones

btn_iniciar = Button(text="Iniciar", command=iniciar_cronometro).grid(column=0, row=3, sticky=W)
btn_reiniciar = Button(text="Reiniciar", command=reiniciar_cronometro).grid(column=1, row=3, sticky=E)




ventana.mainloop()