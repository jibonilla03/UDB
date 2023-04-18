from tkinter import *

ventana = Tk()
ventana.title("INICIO DE SESION")
ventana.geometry("250x150")

# Las etiquetas las vamos a nombrar siempre iniciando con lbl
lbl_usuario = Label(ventana, text="Usuario", font=("Garamond", 12))
lbl_usuario.pack(anchor=W, padx=10, pady=5)

# Las cajas de texto las vamos a nombrar siempre iniciando con txt
txt_usuario = Entry()
txt_usuario.pack(anchor=W, padx=10, fill=X)

lbl_pass=Label(ventana, text="Contraseña", font=("Garamond", 12))
lbl_pass.pack(anchor=W, padx=10)

txt_pass = Entry(show="*")
txt_pass.pack(anchor=W, padx=10, fill=X)


# Para los botones vamos a nombrar siempre con btn
btn_iniciar_sesion= Button(text="Iniciar Sesion")
btn_iniciar_sesion.pack(anchor=E, padx=10, pady=5)

# Una forma alternativa para crear y ubicar el boton en una sola linea de codigo es la siguiente:
# Button(text="Iniciar sesion").pack(anchor=E, padx=10, pady=5)

ventana.mainloop()