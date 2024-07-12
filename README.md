# Gestor de Productos para Almacén

Este programa en Python permite gestionar productos dentro de un almacén, proporcionando funcionalidades básicas como agregar, eliminar, actualizar y visualizar productos, así como autenticación de usuarios.

## Características

- **Autenticación de Usuarios:** Permite a los usuarios autenticarse utilizando nombre de usuario y contraseña.
- **Gestión de Productos:** Permite agregar nuevos productos, eliminar productos existentes, actualizar información de productos y visualizar la lista de productos disponibles.
- **Almacenamiento Persistente:** Utiliza archivos JSON y Pickle para almacenar usuarios y productos de manera persistente entre sesiones.

## Funcionalidades Implementadas

### Autenticación de Usuarios

Los usuarios pueden iniciar sesión proporcionando su nombre de usuario y contraseña. Se utiliza cifrado SHA-256 para almacenar contraseñas de forma segura.

### Gestión de Productos

- **Agregar Producto:** Permite agregar un nuevo producto con nombre, marca, descripción, precio y stock.
- **Eliminar Producto:** Permite eliminar un producto existente utilizando su código único.
- **Actualizar Producto:** Permite actualizar la información de un producto existente, incluyendo nombre, marca, descripción, precio y stock.
- **Visualizar Productos:** Muestra la lista completa de productos disponibles en el almacén.

### Almacenamiento de Datos

- **Usuarios:** Se almacenan los usuarios registrados utilizando archivos Pickle para persistencia.
- **Productos:** Se utilizan archivos JSON para almacenar la información detallada de cada producto, incluyendo el nombre de usuario asociado a cada producto.

---

Quiero expresar mi profundo agradecimiento a Codo a Codo 4.0 por su valioso tiempo y dedicación en mi aprendizaje, especialmente a María, mi profesora, por su guía constante y apoyo incondicional.
