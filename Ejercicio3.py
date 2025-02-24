"""
Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero 
tabla-n.txt con la tabla de multiplicar de ese número, y muestre por pantalla 
la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por 
pantalla informando de ello.
"""
import os
import datetime

while True:
    inicio = datetime.datetime.now()
    a=True
    while a==True:
        n = input("introduce numero de tabla: ")
        m = input("Introduce número de fila (0-10): ")
        if int(m) > 10:
            print("fila mayor a 10, vuelva a intentar")
        if os.path.exists("tabla-"+n+".txt") == False:
            print("No existe tabla del "+n)
        if int(m) < 11 and os.path.exists("tabla-"+n+".txt"):
            a=False
          
    fyle = open("tabla-"+n+".txt", "r")

    print("\n"+fyle.readlines()[int(m)])

    fyle.close()
    final = datetime.datetime.now()
    print("El tiempo de ejecucion:", (final-inicio))