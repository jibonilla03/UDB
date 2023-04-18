from tkinter import *
# Ubicacion de elementos con place

ventana = Tk()
ventana.title("Ejemplo de uso de place")
ventana.geometry("300x100")

lbl_nombre = Label(ventana, text="Nombre", font=("Arial",14))
lbl_nombre.place(x=10, y=10)

# Tarea para la sesion del miercoles diseñar la ventana de inicio de sesion
# haciendolo con el metodo place

ventana.mainloop()