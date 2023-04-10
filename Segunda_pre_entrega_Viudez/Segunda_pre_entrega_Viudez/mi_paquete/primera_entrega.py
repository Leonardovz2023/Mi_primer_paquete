import os

# Función para registrar usuarios
def registrar_usuario(usuario, contrasena, usuarios):
    if usuario in usuarios:
        print("El usuario ya existe.")
    else:
        usuarios[usuario] = contrasena
        with open("usuarios.txt", "a") as f:
            f.write(usuario + ":" + contrasena + "\n")
        print("Usuario registrado con éxito.")

# Función para mostrar usuarios
def mostrar_usuarios(usuarios):
    print("Usuarios registrados:")
    for usuario in usuarios:
        print(usuario)

# Función para hacer login
def login(usuario, contrasena, usuarios):
    if usuario not in usuarios:
        print("El usuario no existe.")
    elif usuarios[usuario] != contrasena:
        print("La contraseña es incorrecta.")
    else:
        print("¡Bienvenido, {}!".format(usuario))

# Verificar si el archivo de usuarios existe y crearlo si no existe
if not os.path.exists("usuarios.txt"):
    with open("usuarios.txt", "w"):
        pass

# Diccionario para almacenar usuarios
usuarios = {}

# Cargar usuarios desde archivo
with open("usuarios.txt", "r") as f:
    for linea in f:
        campos = linea.strip().split(":")
        if len(campos) == 2:
            usuario, contrasena = campos
            usuarios[usuario] = contrasena

# Imprimir contenido del diccionario usuarios para verificar que se cargaron correctamente
print("Usuarios cargados:")
print(usuarios)

# Menú principal
while True:
    print("\n¿Qué acción desea realizar?")
    print("1. Registrar usuario")
    print("2. Mostrar usuarios")
    print("3. Hacer login")
    print("4. Salir")

    opcion = input("> ")

    if opcion == "1":
        print("\nIngrese el nombre de usuario y la contraseña:")
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")
        registrar_usuario(usuario, contrasena, usuarios)
    elif opcion == "2":
        mostrar_usuarios(usuarios)
    elif opcion == "3":
        print("\nIngrese el nombre de usuario y la contraseña:")
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")
        login(usuario, contrasena, usuarios)
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida.")
