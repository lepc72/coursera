red = ("""
       
                         __       _______  _____      ______ ______   ___ 
                        |  |     |   ____||   _  \   /      |____  | |__ \  
                        |  |     |  |__   |  |_)  | |  ,----'   / /     ) | 
                        |  |     |   __|  |   ___/  |  |       / /     / /  
                        |  `----.|  |____ |  |      |  `----. / /     / /_  
                        |_______||_______|| _|       \______|/_/     |____| 
                                                                            
         """)

print("HOLA TODOS, SEAN BIENVENIDOS A:" ,  red,    "DISFRUTEN SU ESTADIA")



nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()
agno = int(input("Para preparar tu perfil, dime en quÃ© aÃ±o naciste. "))
edad = 2020-agno
print()
estatura = float(input("CuÃ©ntame mÃ¡s de ti, para agregarlo a tu perfil. Â¿CuÃ¡nto mides? DÃ­melo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )

num_amigos = int(input("Muy bien. Finalmente, cuÃ©ntame cuantos amigos tienes. "))
genero = input("ingresa tu genero")
print("muy bien tu genero es:",  genero)
telefono = int(input("Escribe tu telefono porfavor"))
print("Muy bien este es tu tel:", telefono)
mail = input("Ingresa tu correo electronico:")
print("tu correo es:", mail)

print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "años")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centimetros")
print("Amigos:  ", num_amigos)
print("correo:  ",   mail         )
print("sexo:        ",  genero)
print("tel:        ",   telefono)
print("--------------------------------------------------")
print("Gracias por la informaciÃ³n. Esperamos que disfrutes con Mi Red")
print()
mensaje = input("Ahora vamos a publicar tu primer mensaje. Â¿QuÃ© piensas hoy? ")
print()
print("--------------------------------------------------")
print(nombre, "dice:", mensaje)
print("--------------------------------------------------")

#Usaremos una variable bool para indicar si el usuario desea continuar
#utilizando el programa o no
continuar = True

#Este ciclo se mantiene en ejecuciÃ³n hasta que el usuario desee salir
while continuar:

    #Solicitamos opciÃ³n al usuario
    escribir_mensaje = str(input("Â¿Deseas escribir un mensaje? (S/N) "))

    #Vamos a aceptar que el usuario ingrese un mensaje cuando escriban "S", "s", o nada
    if escribir_mensaje == "S" or escribir_mensaje == "s" or escribir_mensaje == "":
        mensaje = input("Vamos a publicar un mensaje. Â¿QuÃ© piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")
    #En caso que sea otra respuesta, vamos a decidir salir.
    #AsÃ­, en la siguiente iteraciÃ³n el ciclo terminarÃ¡
    else:
        continuar = False

#Mensaje de salida, una vez que el ciclo ha terminado.
print("Gracias por usar Mi Red. Â¡Hasta pronto!")

#Ahora puedes escribir mensajes todas las veces que quieras.
#Observa que hemos utilizado un ciclo while que permite repetir la acciÃ³n de preguntar por un mensajes
#hasta que el usuario escribe algo distino de "S".

#Pero las redes sociales pueden ejecutar mÃ¡s acciones que solamente enviar mensajes.

#Te proponemos los siguientes desafÃ­os:
#1. Este programa termina cada vez que el valor de 'escribir_mensaje' es distinto a "S" o a "s".
#   Modifique el programa para que el programa termine UNICAMENTE cuando se ingresa "N" o "n".
#   En caso que se ingrese algo distinto, debe volver a solicitar una opciÃ³n al usuario.
#
#2. Modifica este menÃº para que le permita el usuario realizar mÃ¡s de una acciÃ³n.
#   Por ejemplo, puedes agregar una acciÃ³n que permita al usuario modificar su nombre.
#Ahora puedes practicar solicitando mÃ¡s datos al usuario. Solo tienes que usar apropiadamente input() y print()
#1. Escribe 3 solicitudes de datos al usuario, por ejemplo sexo, numero de telefono, ciudad donde vive,
#   pais de nacimiento, direccion, etc. Guarda esos datos en variables del tipo, y finalmente escrÃ­belos en pantalla
#   utilizando print. Puedes agregar todas las lÃ­neas que necesites.