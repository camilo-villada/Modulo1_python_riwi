while True:
    nombre_producto = input("Ingrese el nombre del producto: ")
    if nombre_producto.isdigit():
        print("Ingrese un dato valido.")
    else:
        break

while True:
    try:
        precio_producto = float(input("Ingrese el precio del producto: "))
        if precio_producto < 0:
            print("Ingrese un dato valido.")
        else:
            break
    except ValueError:
        print("Ingrese un dato valido.")

while True:
    try:
        cantidad_producto = int(input("Ingrese la cantidad del producto: "))
        if cantidad_producto < 0:
            print("Ingrese un dato valido.")
        else:
            break
    except ValueError:
        print("Ingrese un dato valido.")

costo_total = precio_producto * cantidad_producto

print(f"Producto: {nombre_producto} | Precio: {precio_producto} | Cantidad: {cantidad_producto} | Total: {costo_total}")