


def adivina( maximo):
    intentos= int (0)
    import random
    numero = random.randint( 0 ,100)
    while True:
        V= int (input ("ingresar numero adivinar "))
        intentos= intentos + 1 
        if V == numero:                                 #si es falso vuelve a import ...
            print ("cantidad de intentos " , intentos)
            break                                   #vuelve a True osea la condicion  y termina el while
        else :  
            if intentos >= maximo :                 #si esto es falso vuelve a import ...
                print ("se te acabaron los intentos wachin")
                break                                           #vuelve a True osea a la condicion y termina el while 

x = int (input("ingresar la cantidad de intentos"))
adivina (x)

