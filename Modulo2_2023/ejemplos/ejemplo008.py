from tkinter import *

ventana = Tk()
ventana.title("Ejemplo del uso de pack")
ventana.geometry("350x200")

lbl_etiqueta1 = Label(ventana, text="Caja #1", font=("Arial", 20), bg="#009FBD", fg="white")
lbl_etiqueta1.pack(ipadx=20, ipady=20, expand=True, fill=BOTH, side=LEFT)

lbl_etiqueta2 = Label(ventana, text="Caja #1", font=("Arial", 20), bg="#393646", fg="white")
lbl_etiqueta2.pack(ipadx=20, ipady=20, expand=True, fill=BOTH, side=LEFT)

ventana.mainloop()