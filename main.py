users = []

def add_user(name, age):
    if age < 0:
        print("Edad no válida")
        return

    user = {}
    user["name"] = name
    user["age"] = age
    users.append(user)

def remove_user(name):
    for i in range(len(users)):
        if users[i]["name"] == name:
            del users[i]  #  Modificación de lista mientras se itera
            print("Usuario eliminado")  
            return
    print("Usuario no encontrado")

def list_users():
    print("Usuarios registrados:")
    for u in users:
        print("Nombre: " + u["name"] + ", Edad: " + str(u["age"]))  # Concatenación en lugar de f-strings

def load_fake_data():
    add_user("Ana", 25)
    add_user("Luis", -3)  # Edad inválida, pero sigue en el flujo
    add_user("Carlos", 40)
    add_user("Ana", 30)  # Duplicados permitidos

def main():
    load_fake_data()
    list_users()
    remove_user("Ana")
    list_users()

main()  # Llamada directa sin if __name__ == "__main__"
