from tkinter import *
#definiendo la funcion encargada de saludar al usuario
def saluda():
    
    lblsaludar = Label(ventana,text="hola " + entradau.get()).grid(row=5, column=0)
    
def despedir() :
    
    lbldespedir = Label(ventana, text="adios "  + entrada.get()).grid(row=6, column=0) 



    
    
ventana = Tk()
ventana.geometry("500x300")
ventana.title("botones")
lblusuario = Label(text = "usuario:",background="yellow").grid(row=0, column=0, sticky=W)
entradau = StringVar()
txtusuario = Entry(ventana,textvariable=entradau).grid(row=0, column=1)
lblnom = Label(text = "nombre:", background="yellow").grid(row=2, column=0, sticky=W)
entrada = StringVar()
txtnom = Entry(ventana,textvariable=entrada).grid(row=2, column=1)
btnsaludar = Button(ventana,text="saludar",command=saluda).grid(row=0, column=3)
btndespedir = Button(ventana,text="despedir", command=despedir).grid(row=2,column=3)

ventana.mainloop()