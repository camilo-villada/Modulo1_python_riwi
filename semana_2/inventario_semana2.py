inventario = []

def agregar_producto():
    
    while True: #bucle principal
        
        #pedir nombre del producto y validar errores
        nombre_producto = input("Ingrese el nombre del producto: ")
        if nombre_producto.isdigit():
            print("Ingrese un producto valido: ")
            continue

        #pedir precio del producto y validar errores
        while True:
            try:
                precio_producto = float(input("Ingrese el precio del producto: "))
                if precio_producto < 0:
                    print("Ingrese un valor valido.")
                    continue
                break
            except ValueError:
                print("Ingrese un valor valido.")

        cantidad = -1
        ##pedir cantidad del producto y validar errores
        while cantidad <= 0:
            try:
                cantidad = int(input("Ingresa la cantidad de productos: "))
                if cantidad <= 0:
                    print("ingrese una cantidad mayor que 0.")
            except ValueError:
                print("Ingrese una cantidad valida.")
                cantidad = -1
    
        #agregar producto al inventario
        producto = {"nombre" : nombre_producto, "precio" : precio_producto, "cantidad" : cantidad}
        inventario.append(producto)
        print("Producto agregado correctamente")
        
        #preguntar si desea agregar otro producto
        while True:
            respuesta = input("Desea agregar otro producto? (s/n)")
            if respuesta == "s":
                break
            elif respuesta == "n":
                return
            else:
                print("Ingrese un valor valido (s/n)")
            
    

def mostrar_inventario():
    #verificar si el inventario esta vacio
    if not inventario:
        print("El inventario esta vacio.")
        return
    
    #mostrar productos del inventario
    for elementos in inventario:
        nombre = elementos["nombre"]
        precio = elementos["precio"]
        cantidad = elementos["cantidad"]
        print(f"Nombre: {nombre} | Precio: {precio} | Cantidad: {cantidad}")


def calcular_productos():
    if not inventario:
        print("El inventario esta vacio.")
        return
    
    total_valor = 0
    total_cantidad = 0

    #calcular valor total y cantidad total de productos
    for productos in inventario:
        total_valor += productos["precio"] * productos["cantidad"]
        total_cantidad += productos["cantidad"]


    #mostrar resultados
    print(f"El valor total del inventario es: {total_valor}")
    print(f"La cantidad total de productos es: {total_cantidad}")


def menu():

    #menu principal
    while True:
        try:
            menu = int(input(
                "1. Agregar producto\n"
                "2. Mostrar inventario\n"
                "3. Calcular estadísticas\n"
                "4. Salir\n"
                ))
            
                
            if menu == 1:
                agregar_producto()
            elif menu == 2:
                mostrar_inventario()
            elif menu == 3:
                calcular_productos()
            elif menu == 4:
                return
            else: 
                print("ingrese una opcion.")
                continue
        except ValueError:
            print("Ingrese una opcion valida")

menu()
