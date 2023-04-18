# Ejemplo del uso del pack para ubicacion de los widgets en el formulario
from tkinter import *

ventana = Tk()
ventana.title("Ejemplo del uso del pack")
# Otra alternativa para definir el tamaño de la ventana
ventana.geometry("350x200")

lbl_etiqueta1 = Label(ventana, text="Caja #1", bg="#009FBD", fg="white")
lbl_etiqueta1.pack(ipadx=10, ipady=10, expand=True, anchor=N)
#lbl_etiqueta1.pack(ipadx=10, ipady=10, expand=True, anchor=NW)

lbl_etiqueta2 = Label(ventana, text="Caja #2", bg="#393646", fg="white")
lbl_etiqueta2.pack(ipadx=10, ipady=10, expand=True, anchor=S)

ventana.mainloop()