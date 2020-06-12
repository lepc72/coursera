def menu():
    
    print("1. dolar")
    print("2. dolar canadiense")
    print("3. libras esterlinas")
    print("4. euro")
    
    print("cuantos pesos tienes?")
    pesos = float(input())
    print("que tipo de cambio desea hacer?")
    cambio = int(input())
    
    if (cambio == 1):
        
        dolares = float(input("a como esta el dolar el dia de hoy?"))
        
        resultado = print("tienes ",  pesos/dolares, "dolares")
        
    if (cambio == 2) :
        
        dolares_canadienses = float(input("a como esta el dolar canadiense hoy?"))  
        
        resultadodc = print("tienes ", pesos/dolares_canadienses, "dolares canadienses")
        
    if (cambio == 3) :
        
        libras_esterlinas = float(input("a como esta la libra esterlina el dia de hoy?"))   
        resultadole = print("tienes ", pesos/libras_esterlinas, "libras esterlinas")
        
    if (cambio == 4) :
        
        euros = float(input("a como esta el euro el dia de hoy?"))
        resultadoe = print("tienes ", pesos/euros, "euros")
        
   
           
        
        
    
    
    
menu()    
    
    
    
    