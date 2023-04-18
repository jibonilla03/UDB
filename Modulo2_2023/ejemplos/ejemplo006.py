# Para crear una applicacion de escritorio importamos el modulo tkinter:
import tkinter

# Utilizar la clase Tk para crear la ventana principal
ventana = tkinter.Tk()
# definimos el tamaño de la ventana
ventana.minsize(width=500, height=500)

# Agregamos un widget utilizando la sintaxis
# widget = NombreWidget(contenedor, **opciones)
lbl_nombre = tkinter.Label(ventana, text="Jimmy Bonilla", background="#BBD6B8")
lbl_nombre.pack()

# Cargamos la imagen:
python_img = tkinter.PhotoImage(file="images/python.png")

# Redimencionamos la imagen:
# Para hacer la imagen mas pequeña utilizamos el metodo subsample
python_img_redimencionada=python_img.subsample(4)
# Para hacer la imagen mas grande utilizamos el metodo zoom
#python_img.zoom(5)

# En un objeto tipo Label voy a mostrar la imagen cargada previamente
lbl_img =tkinter.Label(ventana, image=python_img_redimencionada)

# Llamar al metodo mainloop() para mantener la ventana desplegada
ventana.mainloop()