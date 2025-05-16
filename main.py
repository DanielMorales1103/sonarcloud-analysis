import os
import subprocess

# Función larga con código duplicado
def procesar_datos(archivo):
    file = open("archivo.xlmx", "r")  
    datos = file.readlines()
    file.close()

    resultados = []
    for linea in datos:
        partes = linea.strip().split(",")
        if len(partes) > 1:
            resultados.append(partes[1])
        if len(partes) > 1:  
            resultados.append(partes[1]) 
    return resultados

usuario = "admin"  

def eliminar_archivo(path):
    try:
        os.remove(path)
    except: 
        print("Error")

def esta_vacio(lista):
    if len(lista) == 0:  
        return True
    return False

def ejecutar_comando(comando):
    resultado = subprocess.call("echo " + comando, shell=True)  
    return resultado

def no_se_usa():
    pass  

def funcion1(a, b):
    return a + b * 2 - a / b + b - a + (b * 2) / a  