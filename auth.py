import pickle
import hashlib


def cargar_usuarios_pickle(archivo="data/usuarios.pickle"):
    try:
        with open(archivo, 'rb') as f:
            usuarios = pickle.load(f)
    except (FileNotFoundError, EOFError) as e:
        print(f"Error al cargar usuarios desde {archivo}: {e}")
        usuarios = {}
    except pickle.UnpicklingError as e:
        print(f"Error al cargar usuarios desde {archivo}: {e}")
        usuarios = {}
    return usuarios

def guardar_usuarios_pickle(usuarios, archivo="data/usuarios.pickle"):
    try:
        with open(archivo, 'wb') as f:
            pickle.dump(usuarios, f)
    except Exception as e:
        print(f"Error al guardar usuarios: {e}")


def obtener_credenciales():
    username = input("Ingrese nuevamente su nombre de usuario: ")
    password = input("Ingrese nuevamente su contraseña: ")
    return username, hash_password(password)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

from auth import hash_password

def autenticar_usuario(usuarios_pickle_path="data/usuarios.pickle"):
    usuarios = cargar_usuarios_pickle(usuarios_pickle_path)  # Cargar los usuarios desde el archivo Pickle
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    hashed_password = hash_password(password)  # Ciframos la contraseña
    if username in usuarios and usuarios[username]["password"] == hashed_password:
        print("Autenticación exitosa.")
        return username  # Devolver el nombre de usuario autenticado
    else:
        print("Autenticación fallida. Usuario o contraseña incorrectos.")
        return None

def registrar_usuario(usuarios):
    usuarios = cargar_usuarios_pickle()  # Cargar los usuarios desde el archivo Pickle
    username, hashed_password = obtener_credenciales()
    if username not in usuarios:
        usuarios[username] = {"username": username, "password": hashed_password}
        guardar_usuarios_pickle(usuarios)  # Guardar los usuarios en el archivo Pickle
        return "Usuario registrado correctamente.", usuarios
    else:
        return "El usuario ya existe.", usuarios