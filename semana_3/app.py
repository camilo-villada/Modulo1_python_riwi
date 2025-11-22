#importar funciones de guardar y cargar CSV
from archivos import guardar_csv, cargar_csv

#lista para almacenar los productos
inventario = []

def nombre_producto(mensaje):

    #validar nombre del producto
    while True:
        nombre = input(mensaje)
        if nombre.isdigit():
            print("Error. Ingrese solo caracteres")
            continue
        return nombre


def precio_producto(mensaje):

    #validar precio del producto
    while True:
        try:
            precio = float(input(mensaje))
            if precio <= 0:
                print("Error. debe ingresar un numero mayor a 0.\n")
                continue
            return precio
        except ValueError:
            print("Ingrese un valor valido.\n")


def cantidad_producto(mensaje):

    #validar cantidad del producto
    while True:
        try:
            cantidad = int(input(mensaje))
            if cantidad <= 0:
                print("Error. debe ingresar un numero mayor a 0.\n")
                continue
            return cantidad
        except ValueError:
            print("Ingrese un valor valido.\n")


def agregar_producto():

    #pedir datos del producto
    nombre = nombre_producto("Ingrese el nombre del producto: ")
    precio = precio_producto("Ingrese el precio del producto: ")
    cantidad = cantidad_producto("Ingrese la cantidad del producto: ")

    #agregar producto al inventario
    inventario.append({'nombre' : nombre, 'precio' : precio, 'cantidad' : cantidad})
    print("producto agregado correctamente")

    #preguntar si desea agregar otro producto
    while True:
        agregar_otro_producto = input("¿Desea agregar otro producto? (s/n)")
        if agregar_otro_producto == 's':
            return agregar_producto()
    
        elif agregar_otro_producto == 'n':
            break
        else:
            print("Ingrese una opcion.")

    #mostrar productos agregados
    for item in inventario:
        print(f"Nombre: {item['nombre']} | Precio: {item['precio']} | Cantidad: {item['cantidad']}\n ")


def mostrar_inventario():

    #verificar si el inventario esta vacio
    if not inventario:
        print("Inventario vacio.")
        return
    
    total = 0

    #mostrar productos del inventario con subtotal
    for item in inventario:
        subtotal = item['precio'] * item['cantidad']
        total += subtotal
        print(f"Nombre: {item['nombre']} | Precio: {item['precio']} | Cantidad: {item['cantidad']} | Subtotal: {subtotal}")
    
    print(f"total inventario: {total}")


def buscar_producto():

    if not inventario:
        print("No hay productos en el inventario.")
        return

    nombre = nombre_producto("Ingrese el nombre del producto: ")
    encontrado = False

    #buscar producto por nombre
    for item in inventario:
        subtotal = item['precio'] * item['cantidad']
        if item['nombre'].lower() == nombre.lower():
            print(f"Nombre: {item['nombre']} | Precio: {item['precio']} | Cantidad: {item['cantidad']} | Total: {subtotal}")
            encontrado = True
            break

    #avisar si no se encontro el producto
    if not encontrado:
        print("Producto no encontrado.")


def actualizar_producto():

    if not inventario:
        print("No hay productos en el inventario.\n")
        return
    
    # Buscar producto por nombre
    nombre = nombre_producto("Ingrese el nombre del producto: ")
    encontrado = False

    #actualizar datos del producto
    for item in inventario:
        if item['nombre'].lower() == nombre.lower():
            
            nuevo_nombre = nombre_producto("Ingrese el nuevo nombre del producto: ")
            nuevo_precio = precio_producto("Ingrese el nuevo precio del producto: ")
            nueva_cantidad = cantidad_producto("Ingrese la nueva cantidad de productos: ")

            item['nombre'] = nuevo_nombre
            item['precio'] = nuevo_precio
            item['cantidad'] = nueva_cantidad

            #mostrar resultados
            print(f"Producto '{nombre}' actualizado correctamente.")
            encontrado = True
            break

    if not encontrado:
        print("Producto no encontrado.")


def eliminar_producto():

    if not inventario:
        print("El inventario esta vacio.")
        return
    
    nombre = nombre_producto("Ingrese el nombre del producto: ")
    encontrado = False

    #eliminar producto por nombre
    for items in inventario:
        if items['nombre'].lower() == nombre.lower():
            inventario.remove(items)
            print(f"Producto {nombre} eliminado correctamente.")

    if not encontrado:
        print("Producto no encontrado.")


def guardar_inventario():

    #guardar inventario en un CSV
    if not inventario:
        print("Inventario vacio. No se puede guardar.")
        return
    ruta = input("Ingrese la ruta para guardar el inventario: ")
    guardar_csv(inventario, ruta)


def cargar_inventario():
    
    """Carga el inventario desde un CSV y pregunta sobrescribir/fusionar"""
    ruta = input("Ingrese la ruta del archivo CSV a cargar: ")
    inv_cargado, filas_invalidas = cargar_csv(ruta)
    if not inv_cargado:
        print("No se cargó ningún producto.")
        return

    while True:
        opcion = input("¿Desea sobrescribir el inventario actual? (s/n): ").lower()
        if opcion == 's':
            inventario.clear()
            inventario.extend(inv_cargado)
            print(f"Inventario sobrescrito. {len(inv_cargado)} productos cargados.")
            if filas_invalidas:
                print(f"{filas_invalidas} filas inválidas omitidas.")
            break
        elif opcion == 'n':
            # Fusionar por nombre
            for p in inv_cargado:
                encontrado = False
                for item in inventario:
                    if item['nombre'].lower() == p['nombre'].lower():
                        item['cantidad'] += p['cantidad']
                        item['precio'] = p['precio']  # actualizar al nuevo precio
                        encontrado = True
                        break
                if not encontrado:
                    inventario.append(p)
            print(f"Inventario fusionado. {len(inv_cargado)} productos cargados.")
            if filas_invalidas:
                print(f"{filas_invalidas} filas inválidas omitidas.")
            break
        else:
            print("Ingrese 's' para sí o 'n' para no.")



def menu():

    #menu principal
    while True:
        try:
            menu_opciones = int(input(
            "1. Agregar producto.\n" 
            "2. Mostrar inventario.\n" 
            "3. Buscar producto.\n" 
            "4. Actualizar producto.\n"
            "5. Eliminar producto.\n"
            "6. Guardar inventario CSV.\n"
            "7. Cargar inventario CSV.\n"
            "8. Salir.\n"
            ""))

        except ValueError:
            print("Ingrese un numero valido\n")
            continue

        if menu_opciones == 1:
            agregar_producto()
        elif menu_opciones == 2:
            mostrar_inventario()
        elif menu_opciones == 3:
            buscar_producto()
        elif menu_opciones == 4:
            actualizar_producto()
        elif menu_opciones == 5:
            eliminar_producto()
        elif menu_opciones == 6:
            guardar_inventario()
        elif menu_opciones == 7:
            cargar_inventario()
        elif menu_opciones == 8:
            break
        else:
            print("Opcion invalida, ingrese una opcion correcta")


menu()

