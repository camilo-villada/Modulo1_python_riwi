import datetime

list_books = [
    {"title": "harry potter", "author" : "j.k. rowling", "category" : "fantasia", "price" : 100000, "quantity" : 10} ,
    {"title": "el señor de los anillos", "author" : "j.r.r tolkien", "category" : "fantasia", "price" : 150000, "quantity" : 10} ,
    {"title": "el alquimista", "author" : "paulo coelho", "category" : "novela", "price" : 120000, "quantity" : 8} ,
    {"title": "el codigo da vinci", "author" : "dan brown", "category" : "novela", "price" : 100000, "quantity" : 10} ,
    {"title": "piense y hagase rico", "author" : "napoleon hill", "category" : "libro de ayuda", "price" : 100000, "quantity" : 5} 
]

#list of registered sales
sales_history = []

#functions for data validation

def title_book(message):

    #It asks for the title and validates that it is not a number.
    while True:
        title = input(message)
        if title.isdigit():
            print("Ingrese solo caracteres.\n")
            continue
        return title
    
def author_book(message):

    #The author requests and verifies that it is not a number
    while True:
        author = input(message)
        if author.isdigit():
            print("Ingrese solo caracteres.\n")
            continue
        return author
    
def category_book(message):

    #It asks for the category and validates that it is not a number.
    while True:
        category = input(message)
        if category.isdigit():
            print("Ingrese solo caracteres.\n")
            continue
        return category
    
def price_book(message):

    #Request the price and check for errors
    while True:
        try:
            price = float(input(message))
            if price < 0:
                print("Error. Ingrese numeros positivos.\n")
                continue
            return price
        except ValueError:
            print("Error.Ingrese un numero valido\n")

def quantity_book(message):

    #requests the quantity and validates for errors
    while True:
        try:
            quantity = int(input(message))
            if quantity < 0:
                print("Ingrese numeros positivos.\n")
                continue
            return quantity
        except ValueError:
            print("Error. Ingrese un numero valido.\n")

#inventory functions

def add_book():

    title = title_book("Ingrese el titulo del libro: ")
    #check if the book exists
    for item in list_books:
        #check if it already exists
        if title.lower() == item["title"].lower():
            print("El producto ya existe.\n")
            return

    #ask for the data
    author = author_book("Ingrese el autor: ")
    category = category_book("Ingrese la categoria: ")
    price = price_book("Ingrese el precio: ")
    quantity = quantity_book("Ingrese la cantidad: ")

    #Create the dictionary and add it to the list.
    book = {
        "title": title,
        "author": author,
        "category": category,
        "price": price,
        "quantity": quantity
    }

    list_books.append(book)
    print("Libro agregado correctamente.\n")

def consult_book():

    #shows available products
    if not list_books:
        print("No hay libros disponibles.\n")
        return
    
    print("\n === Libros ===")
    for item in list_books:
        print(f"Titulo: {item['title']} | Autor: {item['author']} | Categoria: {item['category']} | Precio: {item['price']} | Cantidad: {item['quantity']}")

    print()

def update_book():
    
    #update the data of a book
    title = title_book("Ingrese el titulo del libro: ")
    found = False
    for item in list_books:
        if item["title"].lower() == title.lower():
            
            item["title"] = title_book("Ingrese el nuevo libro: ")
            item["author"] = author_book("Ingrese el nuevo autor: ")
            item["category"] = category_book("Ingrese la nueva categoria: ")
            item["price"] = price_book("Ingrese el nuevo precio: ")
            item["quantity"] = quantity_book("Ingrese la nueva cantidad: ")
            print("Libro actualizado correctamente.\n")
            found = True
            break

    if not found:
        print("Producto no encontrado\n")

def remove_book():

    #delete a book
    title = title_book("Ingrese nombre del libro que desea eliminar: ")
    found = False

    for item in list_books:
        if item["title"].lower() == title.lower():
            list_books.remove(item)
            print(f"Libro {title} eliminado.\n")
            found = True
            break

    if not found:
        print("Producto no encontrado.\n")

#sales management functions

def add_sale():

    # Register a new sale
    print("\n=== Registrar venta ===")
    title = title_book("Ingrese el nombre del libro: ")
    found = False

    # Search for the book in the list
    for item in list_books:
        if item["title"].lower() == title.lower():
            try:
                quantity = int(input("Ingrese la cantidad vendida: "))
            except ValueError:
                print("Cantidad invalida.\n")
                return
            
            # Quantity validations
            if quantity <= 0:
                print("La cantidad debe ser mayor que cero.\n")
                return
            if quantity > item["quantity"]:
                print("No hay suficiente stock.\n")
                return
            
            # Customer data
            customer_name = input("Ingrese el nombre del cliente: ")
            customer_type = input("Ingrese el tipo de cliente (normal/premium): ").lower()

            # If the customer is a premium member, a 10% discount applies.
            discount = 0.1 if customer_type == "premium" else 0
            total_gross = quantity * item["price"]
            total_net = total_gross * (1 - discount)

            # Update product stock
            item["quantity"] -= quantity

            # Save the sale to the history
            sale = {
                "title": item["title"],
                "quantity": quantity,
                "total_gross": total_gross,
                "total_net": total_net,
                "customer_name": customer_name,
                "customer_type": customer_type,
                "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "discount": discount
            }

            sales_history.append(sale)

            # show result
            print("\n Venta registrada correctamente.")
            print(f"Titulo: {item['title']} | Cantidad: {item['quantity']} | Bruto: {total_gross} | Descuento: {discount*100}% | Neto: {total_net}\n")
            found = True
            break

    if not found:
        print("Producto no encontrado.\n")

def show_sales():

    # Shows all recorded sales
    if not sales_history:
        print("No hay ventas registradas.\n")

    print("\n=== Historial de ventas ===")
    for sale in sales_history:
        print(f"Titulo: {sale['title']} | Cantidad: {sale['quantity']} | Cliente: {sale['customer_name']} | "
            f"Tipo: {sale['customer_type']} | Bruto: {sale['total_gross']} | Neto: {sale['total_net']} | "
            f"Descuento: {sale['discount']*100}% | Fecha: {sale['date']} ")
        
    print()

#reporting functions

def count_sales_by_author(sales_history):

    #Count how many units have been sold per book
    sales_count = {}
    for sale in sales_history:
        title = sale["title"]
        quantity = sale["quantity"]
        sales_count[title] = sales_count.get(title, 0) + quantity
    return sales_count

def top_3_best_sellers():

    # Show the 3 best-selling products
    if not sales_history:
        print("No hay ventas registradas: ")
        return
    
    sales_count = count_sales_by_author(sales_history)
    sorted_sales = sorted(sales_count.items(), key=lambda x: x[1], reverse=True)
    top_3 = sorted_sales[:3]

    print("\n=== Top 3 libros mas vendidos ===")
    for i, (title, quantity) in enumerate(top_3, start=1):
        print(f"{i} | {title} - {quantity} unidades")
    print()
    
def author_sales_report():

    # sales by author
    if not sales_history:
        print("No hay ventas registradas.\n")
        return
    
    author_sales = {}

    for sale in sales_history:
        title_name = sale["title"]
        quantity = sale["quantity"]
        author = None

        # Find the author of the sold book
        for item in list_books:
            if item["title"].lower() == title_name.lower():
                author = item["author"]
                break
        
        # Add up sales per author
        if author:
            author_sales[author] = author_sales.get(author, 0) + quantity

    print("\n=== Informe de ventas de autor ===")
    for author, quantity in author_sales.items():
        print(f"{author} : {quantity} unidades")
    print()

def sales_income_report():

    # Calculate gross and net income from all sales
    if not sales_history:
        print("No hay ventas registradas.\n")
        return
    
    total_gross = sum(map(lambda s: s['total_gross'], sales_history))
    total_net = sum(map(lambda s: s['total_net'], sales_history))

    print("\n=== informe de ingresos por ventas ===")
    print(f"Total bruto totales: {total_gross}")
    print(f"Total neto totales: {total_net}")

#menu

def menu():
    while True:
        try:

            menu_op = int(input(
                "1. Agregar nuevo libro.\n"
                "2. Ver libros del inventario.\n"
                "3. Actualizar datos de un libro.\n"
                "4. Eliminar un libro.\n"
                "5. Registrar venta.\n"
                "6. Ver historial de ventas.\n"
                "7. Ver los 3 productos mas vendidos.\n"
                "8. Reporte de ventas por autor.\n"
                "9. Reporte de ingresos brutos y netos.\n"
                "10. Salir.\n"
            ))

            if menu_op == 1:
                add_book()
            elif menu_op == 2:
                consult_book()
            elif menu_op == 3:
                update_book()
            elif menu_op == 4:
                remove_book()
            elif menu_op == 5:
                add_sale()
            elif menu_op == 6:
                show_sales()
            elif menu_op == 7:
                top_3_best_sellers()
            elif menu_op == 8:
                author_sales_report()
            elif menu_op == 9:
                sales_income_report()
            elif menu_op == 10:
                print("Saliendo...")
                break
            else:
                print("Ingrese una opcion valida.\n")
        except ValueError:
            print("Ingrese una opcion valida.\n")

menu()

