from users import users_list

def login():
    user = input("Escriba el nombre de usuario: ")
    password = input("Escriba la contraseña: ")
    msg = "Usuario inexistente"
    
    for u in users_list:
        if user == u[1]:
            if password == u[2]:
                # Acceso aprobado para el usuario
                print("Acceso permitido")
                msg = "El usuario " + user + " inició sesión exitosamente"
                anlisis()
            else:
                print("Acceso denegado")
                msg = "Contraseña incorrecta"
                break
    print(msg)
    
if __name__ == "__main__":
    anlisis()