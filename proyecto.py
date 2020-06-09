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

#Ahora puedes practicar solicitando mÃ¡s datos al usuario. Solo tienes que usar apropiadamente input() y print()
#1. Escribe 3 solicitudes de datos al usuario, por ejemplo sexo, numero de telefono, ciudad donde vive,
#   pais de nacimiento, direccion, etc. Guarda esos datos en variables del tipo, y finalmente escrÃ­belos en pantalla
#   utilizando print. Puedes agregar todas las lÃ­neas que necesites.