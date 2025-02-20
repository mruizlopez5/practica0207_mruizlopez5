"""
Escribir una función que pida un número entero entre 1 y 10, lea el fichero 
tabla-n.txt con la tabla de multiplicar de ese número, donde n es el número 
introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar 
un mensaje por pantalla informando de ello.
"""
import os

while True:
    numero = input("Introduce un numero: ")
    if os.path.exists("tabla-"+numero+".txt"):

        artxibo = open("tabla-"+numero+".txt", "r")
        print(artxibo.read())
        artxibo.close()
    else:
        print("no existe")