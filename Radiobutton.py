from tkinter import *

def mostrar_seleccion():
    seleccion = opcion.get()
    etiqueta_resultado.config(text="Has seleccionado: " + seleccion)

# Crear una ventana
ventana = Tk()
ventana.title("Radio Buttons")
ventana.configure(bg='red')

# Variable para almacenar la selección del usuario
opcion = StringVar()

# Crear un marco
marco = Frame(ventana, bg='black',bd= 22,relief=SUNKEN)
marco.pack(padx= 20,pady=20)

# Etiqueta para el marco
etiqueta_marco = Label(marco, text="¿Elige una opción?")
etiqueta_marco.pack()

# Crear radio buttons
radio_button1 = Radiobutton(marco, text="Opción 1", variable=opcion, value="Opción 1")
radio_button2 = Radiobutton(marco, text="Opción 2", variable=opcion, value="Opción 2")
radio_button3 = Radiobutton(marco, text="Opción 3", variable=opcion, value="Opción 3")

# Botón para mostrar la selección
boton_mostrar = Button(ventana, text="Mostrar Selección", command=mostrar_seleccion)

# Etiqueta para mostrar el resultado
etiqueta_resultado = Label(ventana, text="",bg='red')

# Colocar los elementos en la ventana
radio_button1.pack()
radio_button2.pack()
radio_button3.pack()
boton_mostrar.pack()
etiqueta_resultado.pack()

# Iniciar el bucle principal
ventana.mainloop()
