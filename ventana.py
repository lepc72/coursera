# importamos modulo tkinter
from tkinter import *
# creamos una ventana
ventana = Tk()
#asignamos un tamaño a la ventana
# geometry("ancho x alto + posX + posY")
ventana.geometry("500x300")
#asignamos un nombre a la ventana
ventana.title("mi primera ventana con etiquetas")
#creamos una etiqeta
lblusuario = Label(text = "usuario:",background="yellow").grid(row=0, column=0, sticky=W)
#creando campo de texto

entrada = StringVar()
txtusuario = Entry(ventana,textvariable=entrada).grid(row=0, column=1)
#etiqyeta
lblnom = Label(text = "nombre:", background="yellow").grid(row=2, column=0, sticky=W)
#creando campo de texto
entrada = StringVar()
txtnom = Entry(ventana,textvariable=entrada).grid(row=2, column=1)
#agregamos la etiqueta lblusuario ala ventana



# inicializamos el procesamiento
# se hace cuando terminamos de crear todos los widgets
ventana.mainloop()

