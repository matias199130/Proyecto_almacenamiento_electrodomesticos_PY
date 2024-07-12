import logging
import json
import os
from entrada_salida.entrada_salida import (
    dar_bienvenida, filtrar_por_marca, informacion_detallada_producto, mostrar_menu, mostrar_menu_visualizacion_stock, pedir_datos_sin_codigo, mostrar_respuesta, confirmar,
    pedir_codigo, actualizar_datos, mostrar_datos, listar_productos, despedir,
    mostrar_error, visualizar_stock, mostrar_menu_inicio_sesion, pedir_credenciales
)
from validaciones.validaciones import validar_nuevo_producto, validar_producto
from auth import hash_password, cargar_usuarios_pickle, guardar_usuarios_pickle, registrar_usuario

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def cargar_datos(archivo="data/datos.json"):
    if os.path.exists(archivo):
        with open(archivo, 'r') as f:
            datos = json.load(f)
            return datos
    return {"usuarios": {}}

def guardar_datos(datos, archivo="data/datos.json"):
    try:
        with open(archivo, 'w') as f:
            json.dump(datos, f, indent=4)
    except Exception as e:
        logging.error(f"Error al guardar datos: {e}")

def guardar_contador(codigo_actual, archivo="data/contador.json"):
    try:
        with open(archivo, 'w') as f:
            json.dump({"contador": codigo_actual}, f, indent=4)
    except Exception as e:
        logging.error(f"Error al guardar el contador: {e}")

def cargar_contador(archivo="data/contador.json"):
    if os.path.exists(archivo):
        with open(archivo, 'r') as f:
            data = json.load(f)
            return data.get("contador", 0)
    return 0

def eliminar_producto(datos, usuario, codigo, contador_codigo):
    productos = datos["usuarios"].get(usuario, {}).get("productos", [])
    producto_encontrado = False
    productos_actualizados = []
    for producto in productos:
        if producto["codigo"] == codigo:
            producto_encontrado = True
        else:
            productos_actualizados.append(producto)
    
    if producto_encontrado:
        datos["usuarios"][usuario]["productos"] = productos_actualizados
        contador_codigo -= 1
        guardar_datos(datos)
        guardar_contador(contador_codigo)
        return "Producto eliminado correctamente.", contador_codigo
    else:
        return "Producto no encontrado.", contador_codigo

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

def main():
    logging.info('Iniciando la aplicación')

    dar_bienvenida()  # Mensaje de bienvenida al inicio de la aplicación

    usuarios = cargar_usuarios_pickle()
    usuario_autenticado = None

    while True:
        opcion_inicio = mostrar_menu_inicio_sesion()
        logging.debug(f'Opción seleccionada en el menú de inicio de sesión: {opcion_inicio}')
        if opcion_inicio == "1":
            usuario_autenticado = autenticar_usuario()
            if usuario_autenticado:
                print("Autenticación exitosa.")
                guardar_usuarios_pickle(usuarios)  # Guardar credenciales después de autenticar
                break
            else:
                logging.warning(f'Autenticación fallida')
                print("Usuario o contraseña incorrectos.")
        elif opcion_inicio == "2":
            username = pedir_credenciales()
            mensaje, usuarios = registrar_usuario(usuarios)  # Asignar el valor de retorno a usuarios
            logging.info(mensaje)
            print(mensaje)
            guardar_usuarios_pickle(usuarios)  # Guardar credenciales después de registrar
        elif opcion_inicio == "3":
            despedir()
            logging.info('Saliendo de la aplicación')
            return
        else:
            mostrar_error()
            logging.warning('Opción no válida en el menú de inicio de sesión')

    contador_codigo = cargar_contador()
    datos = cargar_datos()

    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            codigo = contador_codigo + 1
            contador_codigo += 1
            guardar_contador(contador_codigo)
            nombre, marca, descripcion, precio, stock = pedir_datos_sin_codigo()
            productos = datos["usuarios"].get(usuario_autenticado, {}).get("productos", [])
            respuesta = validar_nuevo_producto(productos, str(codigo))
            if respuesta is not None:
                mostrar_respuesta(respuesta)
            else:
                producto = {
                    "codigo": str(codigo),
                    "nombre": nombre,
                    "marca": marca,
                    "descripcion": descripcion,
                    "precio": precio,
                    "stock": stock
                }
                if usuario_autenticado not in datos["usuarios"]:
                    datos["usuarios"][usuario_autenticado] = {"productos": []}
                datos["usuarios"][usuario_autenticado]["productos"].append(producto)
                guardar_datos(datos)
                confirmar()
        elif opcion == "2":
            codigo = pedir_codigo()
            respuesta, contador_codigo = eliminar_producto(datos, usuario_autenticado, codigo, contador_codigo)
            mostrar_respuesta(respuesta)
            confirmar()
        elif opcion == "3":
            codigo = pedir_codigo()
            productos = datos["usuarios"].get(usuario_autenticado, {}).get("productos", [])
            respuesta = validar_producto(productos, codigo)
            if respuesta is not None:
                mostrar_respuesta(respuesta)
            else:
                datos_actualizados = actualizar_datos(productos, codigo)
                for producto in productos:
                    if producto["codigo"] == codigo:
                        producto.update({
                            "nombre": datos_actualizados[1],
                            "marca": datos_actualizados[2],
                            "descripcion": datos_actualizados[3],
                            "precio": datos_actualizados[4],
                            "stock": datos_actualizados[5],
                        })
                guardar_datos(datos)
                confirmar()
        elif opcion == "4":
            codigo = pedir_codigo()
            productos = datos["usuarios"].get(usuario_autenticado, {}).get("productos", [])
            respuesta = validar_producto(productos, codigo)
            if respuesta is not None:
                mostrar_respuesta(respuesta)
            else:
                for producto in productos:
                    if producto["codigo"] == codigo:
                        mostrar_datos(producto)
        elif opcion == "5":
            productos = datos["usuarios"].get(usuario_autenticado, {}).get("productos", [])
            listar_productos(productos)
        elif opcion == "6":
            productos = datos["usuarios"].get(usuario_autenticado, {}).get("productos", [])
            while True:
                opcion_stock = mostrar_menu_visualizacion_stock()
                if opcion_stock == "1":
                    visualizar_stock(productos)
                elif opcion_stock == "2":
                    filtrar_por_marca(productos)
                elif opcion_stock == "3":
                    informacion_detallada_producto(productos)
                elif opcion_stock == "4":
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")
        elif opcion == "7":
            despedir()
            break
        else:
            mostrar_error()

if __name__ == "__main__":
    main()
