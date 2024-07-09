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
    print("6. Salir")
    return input("Indique la operación a realizar: ")

def pedir_datos_sin_codigo():
    nombre = input("Ingrese el nombre del producto: ").title()
    descripcion = input("Ingrese la descripción del producto: ").title()
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese la cantidad en stock del producto: "))
    return nombre, descripcion, precio, stock

def mostrar_respuesta(mensaje):
    print(mensaje)

def confirmar():
    print("Operación realizada correctamente.")

def pedir_codigo():
    codigo = input("Ingrese el código del producto: ")
    return codigo

def actualizar_datos(productos, codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            print(f"Nombre: {producto['nombre']}")
            nombre_actualizado = input("Ingrese el nuevo nombre o presione <Enter> para aceptar: ") or producto["nombre"]
            print(f"Descripción: {producto['descripcion']}")
            descripcion_actualizada = input("Ingrese la nueva descripción o presione <Enter> para aceptar: ") or producto["descripcion"]
            print(f"Precio: {producto['precio']}")
            precio_actualizado = input("Ingrese el nuevo precio o presione <Enter> para aceptar: ") or producto["precio"]
            print(f"Stock: {producto['stock']}")
            stock_actualizado = input("Ingrese la nueva cantidad en stock o presione <Enter> para aceptar: ") or producto["stock"]
        return codigo, nombre_actualizado, descripcion_actualizada, float(precio_actualizado), int(stock_actualizado)

def mostrar_datos(producto):
    etiquetas = ["Código", "Nombre", "Descripción", "Precio", "Stock"]
    print("=" * 40)
    for etiqueta, valor in zip(etiquetas, producto.values()):
        print(f"{etiqueta}: {valor}")
    print("=" * 40)

def listar_productos(productos):
    print("\nLista de productos")
    print(f"{'Código':<10} {'Nombre':<20} {'Descripción':50} {'Precio':<20} {'Stock':<20}")
    print("=" * 110)
    for producto in productos:
        print(f"{producto['codigo']:<10} {producto['nombre']:<20} {producto['descripcion']:<50} {producto['precio']:<20} {producto['stock']:<20}")

def despedir():
    print("Gracias por utilizar este sistema.")
    print("Hasta luego")

def mostrar_error():
    print("ERROR")
    print("Por favor, verifique la opción ingresada e intente nuevamente.")

