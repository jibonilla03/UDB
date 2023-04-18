from tkinter import *

ventana = Tk()
ventana.title("Ejemplo de uso de Grid")
ventana.geometry("300x180")

lbl_usuario = Label(ventana, text="Usuario", font=("Arial", 14))
lbl_usuario.grid(column=0, row=0, padx=10, pady=5, sticky=W)

txt_usuario = Entry()
txt_usuario.grid(column=0, row=1, padx=10)

lbl_pass = Label(ventana, text="Contraseña", font=("Arial", 14))
lbl_pass.grid(column=0, row=2, padx=10, pady=10, sticky=W)

txt_usuario = Entry(show="*")
txt_usuario.grid(column=0, row=3, padx=10)

Button(text="Iniciar Sesion").grid(column=0, row=4, sticky=W, padx=10, pady=10)

ventana.mainloop()