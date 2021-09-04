
#el archivo __init__  tiene que declararse , no tiene que tener nada , 
# y es condicion para declarar una carpeta como paquete



# "programa Madre" tiene que estar afuera del la CARPETA "Paquete ""..

from Paquete import  funcion1  #desde la carpeta paquete traeme el programa " funcion1"
from Paquete import funcion2



funcion2.funcion()
funcion1.funcion ()  # desde el programa "funcion1"  mostrame esa funcion que tiene adentro
