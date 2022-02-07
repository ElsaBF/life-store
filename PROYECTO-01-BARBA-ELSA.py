# Del archivo users.py importamos la lista llamada users_list
from users import users_list

# Definimos una función para realizar el login
def login():
    mensaje_bienvenida = "Bienvenido, por favor ingresa tus credenciales para acceder al sistema."
    print(mensaje_bienvenida)
    user = input("Escriba el nombre de usuario: ")
    password = input("Escriba la contraseña: ")
    msg = "Usuario inexistente"

    for u in users_list:
        if user == u[1]:
            if password == u[2]:
                # Acceso aprobado para el usuario
                print("Acceso permitido")
                msg = "El usuario " + user + " inició sesión exitosamente"
                ##### Aquí va el nombre de la función a la que acceder en caso de que las credenciales sean válidas
            else:
                print("Acceso denegado")
                msg = "Contraseña incorrecta"
                break
    print(msg)
    
if __name__ == "__main__":
    login()