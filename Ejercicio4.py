"""
Escribir un programa que acceda al fichero de internet mediante 
la url indicada y muestre por pantalla el número de palabras 
que contiene.
http://textfiles.com/adventure/aencounter.txt 
"""
import urllib.request
import datetime



def read_url(url):
    palabras=0
    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")
        palabras=palabras+palabras_linea(decoded_line) #suma de fondo las palabras de cada linea
        print(palabras_linea(decoded_line)) #imprime recuento de palabras en linea
        print(decoded_line) #imprime linea

    print("palabras totales:",palabras )
    return 0


def palabras_linea(linea):
    cuenta=0
    previo=False
    prueba=False

    for caracter in linea:

        if caracter>"@" and caracter<"[" or caracter>"`"and caracter<"{": #para todos los casos que caracter sea letra entra
            previo=prueba #previo almacena el valor anterior de prueba
            prueba=True #el caracter analizado es una letra y prueba pasa a true
            
            if previo != prueba: #si el valor previo es false y la prueba es true significa que HA DETECTADO EL INICIO DE UNA PALABRA
                cuenta=cuenta+1 
            
        else:
            previo=prueba #previo almacena el valor anterior de prueba
            prueba=False #el caracter analizado NO es una letra y prueba es False
        

    return cuenta



url = "http://textfiles.com/adventure/aencounter.txt"
read_url(url)

