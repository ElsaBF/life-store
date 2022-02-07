# Del archivo users.py importamos la lista llamada users_list
from users import users_list

### Definimos una función para realizar el login
def login():
    # Se muestra un mensaje de bienvenida para el usuario
    mensaje_bienvenida = "Bienvenido, por favor ingresa tus credenciales para acceder al sistema."
    print(mensaje_bienvenida)
    # Se solicitan nombre de usuario y contraseña
    user = input("Escriba el nombre de usuario: ")
    password = input("Escriba la contraseña: ")
    # Este mensaje se utiliza si el usuario no es encontrado en la lista
    msg = "Usuario inexistente"

    for u in users_list:
        # Este if busca que el usuario exista y esté registrado en la posición [1] de la lista
        if user == u[1]:
            # Aquí se busca que la contraseña exista en la base de datos y coincida con el usuario 
            if password == u[2]:
                # Acceso aprobado para el usuario
                print("Acceso permitido")
                msg = "El usuario " + user + " inició sesión exitosamente"
                #Aquí va el nombre de la función a la que acceder en caso de que las credenciales sean válidas
                analisis()
            # Si la contraseña es incorrecta se pasa a esta sección
            else:
                print("Acceso denegado")
                msg = "Contraseña incorrecta"
                break
    # Si el usuario no existe se muestra el mensaje
    print(msg)

### Definimos una función para comenzar el análisis de los datos
def analisis():
    options = input("Por favor elige a qué información quieres acceder: ")
    
if __name__ == "__main__":
    login()