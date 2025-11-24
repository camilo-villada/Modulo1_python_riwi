import datetime   # Librería para manejar fechas y horas

# Lista inicial de productos precargados

list_products = [
    {"name": "computer", "brand": "dell", "category": "electronics", "price": 2500000, "stock": 10, "warranty": 24},
    {"name": "phone", "brand": "iphone", "category": "electronics", "price": 2000000, "stock": 15, "warranty": 12},
    {"name": "tv", "brand": "lg", "category": "appliances", "price": 1500000, "stock": 8, "warranty": 18},
    {"name": "fridge", "brand": "samsung", "category": "appliances", "price": 1000000, "stock": 5, "warranty": 36},
    {"name": "earphones", "brand": "sony", "category": "accessories", "price": 300000, "stock": 20, "warranty": 6}
]

# Lista donde se guardan todas las ventas registradas
sales_history = []


# Funciones de validación de entradas

def name_product(message):
    # Pide un nombre y valida que no sea un número
    while True:
        name = input(message)
        if name.isdigit():
            print("Error. You must enter letters.\n")
            continue
        return name

def brand_product(message):
    # Pide una marca y valida que no sea un número
    while True:
        brand = input(message)
        if brand.isdigit():
            print("Error. You must enter letters.\n")
            continue
        return brand

def category_product(message):
    # Pide una categoría y valida que no sea un número
    while True:
        category = input(message)
        if category.isdigit():
            print("Error. You must enter letters.\n")
            continue
        return category

def price_product(message):
    # Pide un precio y valida que sea mayor a 0
    while True:
        try:
            price = float(input(message))
            if price <= 0:
                print("Error. Price must be greater than 0.\n")
                continue
            return price
        except ValueError:
            print("Enter a valid number.\n")

def stock_products(message):
    # Pide cantidad en stock y valida que sea número positivo
    while True:
        try:
            stock = int(input(message))
            if stock < 0:
                print("Error. Stock must be 0 or more.\n")
                continue
            return stock
        except ValueError:
            print("Enter a valid number.\n")

def warranty_products(message):
    # Pide garantía en meses y valida que sea mayor a 0
    while True:
        try:
            warranty = int(input(message))
            if warranty <= 0:
                print("Error. Warranty must be greater than 0.\n")
                continue
            return warranty
        except ValueError:
            print("Enter a valid number.\n")


# Funciones de inventario

def add_products():
    # Agrega un nuevo producto al inventario
    name = name_product("Enter the product name: ")
    # Verifica que no exista ya
    for item in list_products:
        if name.lower() == item["name"].lower():
            print("The product already exists.\n")
            return
    
    # Pide los demás datos del producto
    brand = brand_product("Enter the brand: ")
    category = category_product("Enter the category: ")
    price = price_product("Enter the price: ")
    stock = stock_products("Enter the quantity: ")
    warranty = warranty_products("Enter the warranty (months): ")

    # Crea el diccionario del producto y lo agrega a la lista
    product = {
        "name": name,
        "brand": brand,
        "category": category,
        "price": price,
        "stock": stock,
        "warranty": warranty
    }
    list_products.append(product)
    print("Product added successfully.\n")

def consult_products():
    # Muestra todos los productos disponibles en inventario
    if not list_products:
        print("No products available.\n")
        return
    
    print("\n=== Product List ===")
    for item in list_products:
        print(f"Name: {item['name']}, Brand: {item['brand']}, Category: {item['category']}, "
              f"Price: {item['price']}, Stock: {item['stock']}, Warranty: {item['warranty']} months")
    print()

def update_products():
    # Permite actualizar los datos de un producto existente
    name = name_product("Enter the product name to update: ")
    found = False
    for item in list_products:
        if item["name"].lower() == name.lower():
            # Pide nuevos valores para cada campo
            item["name"] = name_product("Enter new name: ")
            item["brand"] = brand_product("Enter new brand: ")
            item["category"] = category_product("Enter new category: ")
            item["price"] = price_product("Enter new price: ")
            item["stock"] = stock_products("Enter new stock: ")
            item["warranty"] = warranty_products("Enter new warranty: ")
            print(f"Product {name} updated successfully.\n")
            found = True
            break
    if not found:
        print("Product not found.\n")

def remove_product():
    # Elimina un producto del inventario
    name = name_product("Enter the product name to remove: ")
    found = False
    for item in list_products:
        if item["name"].lower() == name.lower():
            list_products.remove(item)
            print(f"Product {name} removed.\n")
            found = True
            break
    if not found:
        print("Product not found.\n")



# Funciones de gestión de ventas

def add_sale():
    # Registra una nueva venta de un producto
    print("\n=== Register Sale ===")
    name = name_product("Enter product name: ")
    found = False

    # Buscar el producto en la lista
    for item in list_products:
        if item["name"].lower() == name.lower():
            try:
                quantity = int(input("Enter quantity sold: "))
            except ValueError:
                print("Invalid quantity.\n")
                return

            # Validaciones de cantidad
            if quantity <= 0:
                print("Quantity must be greater than zero.\n")
                return
            if quantity > item["stock"]:
                print("Not enough stock.\n")
                return
            
            # Datos del cliente
            customer_name = input("Enter customer name: ")
            customer_type = input("Enter customer type (regular/premium): ").lower()
            
            # Si el cliente es premium, se aplica 10% de descuento
            discount = 0.1 if customer_type == "premium" else 0
            total_gross = quantity * item["price"]   # Precio sin descuento
            total_net = total_gross * (1 - discount) # Precio con descuento
            
            # Actualizar stock del producto
            item["stock"] -= quantity
            
            # Guardar la venta en el historial
            sale = {
                "product": item["name"],
                "quantity": quantity,
                "total_gross": total_gross,
                "total_net": total_net,
                "customer_name": customer_name,
                "customer_type": customer_type,
                "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "discount": discount
            }
            sales_history.append(sale)
            
            # Mostrar confirmación
            print("\nSale registered successfully!")
            print(f"Product: {item['name']}, Quantity: {quantity}, Gross: {total_gross}, "
                  f"Discount: {discount*100}%, Net: {total_net}\n")
            found = True
            break

    if not found:
        print("Product not found.\n")


def show_sales():
    # Muestra todas las ventas registradas
    if not sales_history:
        print("No sales registered.\n")
        return
    
    print("\n=== Sales History ===")
    for sale in sales_history:
        print(f"Product: {sale['product']}, Quantity: {sale['quantity']}, Customer: {sale['customer_name']}, "
              f"Type: {sale['customer_type']}, Gross: {sale['total_gross']}, Net: {sale['total_net']}, "
              f"Discount: {sale['discount']*100}%, Date: {sale['date']}")
    print()



# Funciones de reportes

def count_sales_by_product(sales_history):
    # Cuenta cuántas unidades se han vendido por producto
    sales_count = {}
    for sale in sales_history:
        product = sale["product"]
        qty = sale["quantity"]
        sales_count[product] = sales_count.get(product, 0) + qty
    return sales_count


def top_3_best_sellers():
    # Muestra los 3 productos más vendidos
    if not sales_history:
        print("No sales registered.\n")
        return
    
    sales_count = count_sales_by_product(sales_history)
    sorted_sales = sorted(sales_count.items(), key=lambda x: x[1], reverse=True)
    top_3 = sorted_sales[:3]
    
    print("\n=== Top 3 Best Sellers ===")
    for i, (product, qty) in enumerate(top_3, start=1):
        print(f"{i}. {product} - {qty} units")
    print()


def brand_sales_report():
    # Agrupa las ventas por marca
    if not sales_history:
        print("No sales registered.\n")
        return
    
    brand_sales = {}
    for sale in sales_history:
        product_name = sale["product"]
        quantity = sale["quantity"]
        brand = None
        
        # Buscar la marca del producto vendido
        for item in list_products:
            if item["name"].lower() == product_name.lower():
                brand = item["brand"]
                break
        
        # Sumar ventas por marca
        if brand:
            brand_sales[brand] = brand_sales.get(brand, 0) + quantity
    
    print("\n=== Brand Sales Report ===")
    for brand, qty in brand_sales.items():
        print(f"{brand}: {qty} units")
    print()


def sales_income_report():
    # Calcula ingresos brutos y netos de todas las ventas
    if not sales_history:
        print("No sales registered.\n")
        return
    
    # Uso de lambda para cumplir requisito del proyecto
    total_gross = sum(map(lambda s: s['total_gross'], sales_history))
    total_net = sum(map(lambda s: s['total_net'], sales_history))
    
    print("\n=== Sales Income Report ===")
    print(f"Total Gross Income: {total_gross}")
    print(f"Total Net Income: {total_net}\n")


def inventory_performance_report():
    # Evalúa el rendimiento del inventario según ventas
    if not sales_history:
        print("No sales registered.\n")
        return
    
    print("\n=== Inventory Performance Report ===")
    for item in list_products:
        # Cantidad vendida de este producto
        sold_qty = sum(sale['quantity'] for sale in sales_history if sale['product'].lower() == item['name'].lower())
        # Cantidad total (vendida + la que queda en stock)
        total_qty = sold_qty + item['stock']
        
        if total_qty > 0:
            performance = (sold_qty / total_qty) * 100
            print(f"{item['name']} - Sold: {sold_qty}, Remaining: {item['stock']}, Performance: {performance:.2f}%")
    print()



def menu():

    while True:
        print("\n=== Main Menu ===")
        print("1. Add product")                     # Agregar un nuevo producto
        print("2. Consult products")                # Ver todos los productos en inventario
        print("3. Update product")                  # Actualizar datos de un producto
        print("4. Remove product")                  # Eliminar un producto
        print("5. Register sale")                   # Registrar una venta
        print("6. Show sales")                      # Ver historial de ventas
        print("7. Top 3 best sellers")              # Ver los 3 productos más vendidos
        print("8. Brand sales report")              # Reporte de ventas agrupadas por marca
        print("9. Sales income report")             # Reporte de ingresos brutos y netos
        print("10. Inventory performance report")   # Reporte de rendimiento del inventario
        print("0. Exit")                            # Salir del programa
        
        try:
            menu_op = int(input("Select an option: "))
        except ValueError:
            print("Enter a valid value.\n")
            continue
       
        if menu_op == 1:
            add_products()
        elif menu_op == 2:
            consult_products()
        elif menu_op == 3:
            update_products()
        elif menu_op == 4:
            remove_product()
        elif menu_op == 5:
            add_sale()
        elif menu_op == 6:
            show_sales()
        elif menu_op == 7:
            top_3_best_sellers()
        elif menu_op == 8:
            brand_sales_report()
        elif menu_op == 9:
            sales_income_report()
        elif menu_op == 10:
            inventory_performance_report()
        elif menu_op == 0:
            # Si elige 0, se termina el programa
            print("Exiting...")
            break
        else:
            # Si escribe un número que no está en el menú
            print("Enter a valid option.\n")


menu()   

