from tkinter import *
ventana = Tk()
ventana.geometry("500x300")
ventana.title("botones")
lblusuario = Label(text = "usuario:",background="yellow").grid(row=0, column=0, sticky=W)
entrada = StringVar()
txtusuario = Entry(ventana,textvariable=entrada).grid(row=0, column=1)
lblnom = Label(text = "nombre:", background="yellow").grid(row=2, column=0, sticky=W)
entrada = StringVar()
txtnom = Entry(ventana,textvariable=entrada).grid(row=2, column=1)
btnsaludar = Button(ventana,text="saludar").grid(row=2, column=3)
btndespedir = Button(ventana,text="despedir").grid(row=0,column=3)

ventana.mainloop()