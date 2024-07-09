def validar_nuevo_producto(productos, codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            return f"Ya existe un producto con el código: {codigo}"
    return None

def validar_producto(productos, codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            return None
    return f"No existe un producto con el código: {codigo}"
