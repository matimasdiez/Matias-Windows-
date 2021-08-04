


def adivinar( V, maximo):
    intentos= int (0)
    while True:
        import random
        numero = random.randint( 0 ,100)
        print ( "numero aleatorios son " , numero)
        intentos= intentos + 1 
        if V == numero:                                 #si es falso vuelve a import ...
            print ("cantidad de intentos " , intentos)
            break                                   #vuelve a True osea la condicion  y termina el while
        else :  
            if intentos >= maximo :                 #si esto es falso vuelve a import ...
                print ("se te acabaron los intentos wachin")
                break                                           #vuelve a True osea a la condicion y termina el while 
adivinar(67, 10)



     
    


