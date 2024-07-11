# auth.py
import os
import hashlib
import pickle

def cargar_usuarios(archivo="data/usuarios.pickle"):
    if os.path.exists(archivo):
        try:
            with open(archivo, 'rb') as f:
                usuarios = pickle.load(f)
                return {usuario["username"]: usuario for usuario in usuarios}
        except EOFError:
            return {}  # Devuelve un diccionario vacío si el archivo está vacío
    return {}  # Devuelve un diccionario vacío si el archivo no existe

def guardar_usuarios(usuarios, archivo="data/usuarios.pickle"):
    try:
        os.makedirs(os.path.dirname(archivo), exist_ok=True)
        with open(archivo, 'wb') as f:
            pickle.dump([{"username": username, "password": usuario["password"]} for username, usuario in usuarios.items()], f)
    except Exception as e:
        print(f"Error al guardar usuarios: {e}")

def obtener_credenciales():
    username = input("Ingrese nuevamente su nombre de usuario: ")
    password = input("Ingrese nuevamente su contraseña: ")
    return username, hash_password(password)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def autenticar_usuario(usuarios):
    usuarios = cargar_usuarios()  # Cargar los usuarios desde el archivo Pickle
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    hashed_password = hash_password(password)  # Ciframos la contraseña
    if username in usuarios and usuarios[username]["password"] == hashed_password:
        print("Autenticación exitosa.")
        return True
    else:
        print("Autenticación fallida. Usuario o contraseña incorrectos.")
        return False

def registrar_usuario(usuarios):
    usuarios = cargar_usuarios()  # Cargar los usuarios desde el archivo Pickle
    username, hashed_password = obtener_credenciales()
    if username not in usuarios:
        usuarios[username] = {"username": username, "password": hashed_password}
        guardar_usuarios(usuarios)  # Guardar los usuarios en el archivo Pickle
        return "Usuario registrado correctamente.", usuarios
    else:
        return "El usuario ya existe.", usuarios