usuarios = []

def agregar_usuario(nombre, edad):
    if edad < 0:
        return  

    user = {"nombre": nombre, "edad": edad}
    usuarios.append(user)

def eliminar_usuario(nombre):
    for i in range(len(usuarios)):
        if usuarios[i]["nombre"] == nombre:
            del usuarios[i]  
            return
    else:
        pass 

def imprimir_usuarios():
    mensaje = ""  
    for u in usuarios:
        mensaje += u["nombre"] + ", edad: " + str(u["edad"]) + "\n"  
    print(mensaje)

def main():
    agregar_usuario("Ana", 22)
    agregar_usuario("Luis", -3) 
    eliminar_usuario(None)  
    imprimir_usuarios()

main()
