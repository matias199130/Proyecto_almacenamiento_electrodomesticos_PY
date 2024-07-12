import json
from auth import cargar_usuarios_pickle, autenticar_usuario, registrar_usuario
""" from entrada_salida.entrada_salida import mostrar_menu_inicio_sesion """

def dar_bienvenida():
    mensaje = """
╔═════════════════════════════════════╗
║        Bienvenido/a al sistema      ║
║   de gestión de electrodomésticos   ║
╚═════════════════════════════════════╝
    """
    print(mensaje)

def mostrar_menu():
    print("\nMenú de Gestión de Productos")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar datos de producto")
    print("4. Ver datos de un producto")
    print("5. Ver todos los productos")
    print("6. Visualizar stock")
    print("7. Salir")
    return input("Indique la operación a realizar: ")

def pedir_datos_sin_codigo():
    nombre = input("Ingrese el nombre del producto: ").title()
    marca = input("Ingrese la marca del producto: ").title()
    descripcion = input("Ingrese la descripción del producto: ").title()
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese la cantidad en stock del producto: "))
    return nombre, marca, descripcion, precio, stock

def mostrar_respuesta(mensaje):
    print(mensaje)

def confirmar():
    print("Operación realizada correctamente.")

def pedir_codigo():
    codigo = input("Ingrese el código del producto: ")
    return codigo

# entrada_salida.py

def mostrar_menu_inicio_sesion():
    print("\nMenú de Inicio de Sesión:")
    print("1. Iniciar sesión")
    print("2. Registrar usuario")
    print("3. Salir")
    return input("Seleccione una opción: ")

def pedir_credenciales():
    username = input("Ingrese nombre de usuario: ")
    password = input("Ingrese contraseña: ")
    return username, password


def mostrar_menu_visualizacion_stock():
    print("\nMenú de Visualización de Stock:")
    print("1. Ver Stock Total")
    print("2. Filtrar por Marca")
    print("3. Información Detallada del Producto")
    print("4. Volver al Menú Principal")
    return input("Seleccione una opción: ")

def visualizar_stock(productos):
    print("Visualización de Stock:")
    print("=" * 130)
    print(f"{'Código':<10} {'Marca':<20} {'Nombre':<20} {'Stock':<10}")
    print("-" * 130)
    
    for producto in productos:
        print(f"{producto['codigo']:<10} {producto['marca']:<20} {producto['nombre']:<20} {producto['stock']:<10}")
    
    print("=" * 130)

def filtrar_por_marca(productos):
    marca = input("Ingrese la marca a filtrar: ").title()
    productos_filtrados = [producto for producto in productos if producto['marca'].title() == marca]
    
    if productos_filtrados:
        print(f"Productos de la marca '{marca}':")
        print("=" * 130)
        print(f"{'Código':<10} {'Marca':<20} {'Nombre':<20} {'Stock':<10}")
        print("-" * 130)
        
        for producto in productos_filtrados:
            print(f"{producto['codigo']:<10} {producto['marca']:<20} {producto['nombre']:<20} {producto['stock']:<10}")
    else:
        print(f"No se encontraron productos de la marca '{marca}'.")

def informacion_detallada_producto(productos):
    codigo = input("Ingrese el código del producto: ")
    producto = next((prod for prod in productos if prod['codigo'] == codigo), None)
    
    if producto:
        print(f"Detalles del Producto {codigo}:")
        print(f"Código: {producto['codigo']}")
        print(f"Marca: {producto['marca']}")
        print(f"Nombre: {producto['nombre']}")
        print(f"Descripción: {producto['descripcion']}")
        print(f"Precio: {producto['precio']}")
        print(f"Stock: {producto['stock']}")
    else:
        print(f"No se encontró un producto con el código '{codigo}'.")

def actualizar_datos(productos, codigo):
    producto = next((prod for prod in productos if prod['codigo'] == codigo), None)
    
    if not producto:
        return None
    
    nombre_actualizado = input(f"Nombre actual ({producto['nombre']}): ") or producto['nombre']
    marca_actualizada = input(f"Marca actual ({producto['marca']}): ") or producto['marca']
    descripcion_actualizada = input(f"Descripción actual ({producto['descripcion']}): ") or producto['descripcion']
    
    try:
        precio_actualizado = input(f"Precio actual ({producto['precio']}): ") or producto['precio']
        precio_actualizado = float(precio_actualizado)
    except ValueError:
        print("Precio inválido, se mantendrá el precio actual.")
        precio_actualizado = producto['precio']
        
    try:
        stock_actualizado = input(f"Stock actual ({producto['stock']}): ") or producto['stock']
        stock_actualizado = int(stock_actualizado)
    except ValueError:
        print("Stock inválido, se mantendrá el stock actual.")
        stock_actualizado = producto['stock']
    
    return codigo, nombre_actualizado, marca_actualizada, descripcion_actualizada, precio_actualizado, stock_actualizado

def mostrar_datos(producto):
    etiquetas = ["Código", "Nombre", "Marca", "Descripción", "Precio", "Stock"]
    print("=" * 130)
    for etiqueta, valor in zip(etiquetas, producto.values()):
        print(f"{etiqueta}: {valor}")
    print("=" * 130)

def listar_productos(productos):
    print("Listado de Productos:")
    print("=" * 130)
    print(f"{'Código':<10} {'Marca':<20} {'Nombre':<20} {'Descripción':<50} {'Precio':<20} {'Stock':<20}")
    print("-" * 130)
    
    for producto in productos:
        print(f"{producto['codigo']:<10} {producto['marca']:<20} {producto['nombre']:<20} {producto['descripcion']:<50} {producto['precio']:<20} {producto['stock']:<20}")

    print("=" * 130)

def despedir():
    print("Gracias por utilizar este sistema.")
    print("Hasta luego")

def mostrar_error():
    print("ERROR")
    print("Por favor, verifique la opción ingresada e intente nuevamente.")
