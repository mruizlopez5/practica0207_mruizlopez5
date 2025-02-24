"""
Escribir una función que pida un número entero entre 1 y 10 y guarde en un 
fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, 
donde n es el número introducido.
"""
import datetime
while True:

    

    numero = input("Introduce un número entero entre 1 y 10: ")
    inicio = datetime.datetime.now()
    titulo = "tabla-"+numero+".txt"
    txt = open(titulo, "w")
    txt.close()
    txt = open(titulo, "a")
    for i in range(11):
        ""
        res = int(numero) * i
        linea = numero+"x"+str(i)+"="+str(res)+"\n"
        txt.write(str(linea))

    txt.close()

    final = datetime.datetime.now()
    print("el tiempo de ejecucuion es:",(final-inicio))

