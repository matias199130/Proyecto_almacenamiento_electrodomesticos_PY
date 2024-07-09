import json
import os
from entrada_salida.entrada_salida import (
    dar_bienvenida, mostrar_menu, pedir_datos_sin_codigo, mostrar_respuesta, confirmar,
    pedir_codigo, actualizar_datos, mostrar_datos, listar_productos, despedir,
    mostrar_error
)
from validaciones.validaciones import validar_nuevo_producto, validar_producto

def guardar_productos(productos, archivo="data/productos.json"):
    with open(archivo, 'w') as f:
        json.dump(productos, f, indent=4)

def cargar_productos(archivo="data/productos.json"):
    if os.path.exists(archivo):
        with open(archivo, 'r') as f:
            return json.load(f)
    return []

def guardar_contador(codigo_actual, archivo="data/contador.json"):
    with open(archivo, 'w') as f:
        json.dump({"contador": codigo_actual}, f, indent=4)

def cargar_contador(archivo="data/contador.json"):
    if os.path.exists(archivo):
        with open(archivo, 'r') as f:
            data = json.load(f)
            return data.get("contador", 0)
    return 0

def main():
    dar_bienvenida()
    
    productos = cargar_productos()
    contador_codigo = cargar_contador()

    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            codigo = contador_codigo + 1
            contador_codigo += 1
            guardar_contador(contador_codigo)
            nombre, descripcion, precio, stock = pedir_datos_sin_codigo()
            respuesta = validar_nuevo_producto(productos, str(codigo))
            if respuesta is not None:
                mostrar_respuesta(respuesta)
            else:
                producto = {"codigo": str(codigo), "nombre": nombre, "descripcion": descripcion, "precio": precio, "stock": stock}
                productos.append(producto)
                guardar_productos(productos)
                confirmar()
        elif opcion == "2":
            codigo = pedir_codigo()
            respuesta = validar_producto(productos, codigo)
            if respuesta is not None:
                mostrar_respuesta(respuesta)
            else:
                productos = [producto for producto in productos if producto["codigo"] != codigo]
                guardar_productos(productos)
                confirmar()
        elif opcion == "3":
            codigo = pedir_codigo()
            respuesta = validar_producto(productos, codigo)
            if respuesta is not None:
                mostrar_respuesta(respuesta)
            else:
                datos_actualizados = actualizar_datos(productos, codigo)
                for producto in productos:
                    if producto["codigo"] == codigo:
                        producto.update({
                            "nombre": datos_actualizados[1],
                            "descripcion": datos_actualizados[2],
                            "precio": datos_actualizados[3],
                            "stock": datos_actualizados[4],
                        })
                guardar_productos(productos)
                confirmar()
        elif opcion == "4":
            codigo = pedir_codigo()
            respuesta = validar_producto(productos, codigo)
            if respuesta is not None:
                mostrar_respuesta(respuesta)
            else:
                for producto in productos:
                    if producto["codigo"] == codigo:
                        mostrar_datos(producto)
        elif opcion == "5":
            listar_productos(productos)
        elif opcion == "6":
            despedir()
            break
        else:
            mostrar_error()

if __name__ == "__main__":
    main()
