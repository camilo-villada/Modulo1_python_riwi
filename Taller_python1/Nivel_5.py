#Nivel 5 — Retos

#25
lista_estudiantes = []

def agregar_estudiante():

    while True:
        nombre = input("Ingrese el nombre del estudiante: ")
        if nombre.isdigit():
            print("Nombre invalido.")
            continue
        break

    while True:
        edad = input("Ingrese la edad del estudiante:")
        if not edad.isdigit():
            print("Edad invalida.")
            continue
        edad = int(edad)
        break

    while True:
        try:
            cantidad_notas = int(input("Ingrese cuantas notas quiere agregar:"))
            if cantidad_notas <= 0:
                print("La cantidad de notas dene ser mayor a cero.")
                continue
            break
        except ValueError:
            print("Cantidad invalida. Ingrese un numero.")

    notas = []
    for i in range(cantidad_notas):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i + 1}: "))
                if 0 <= nota <= 100:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 100.")
            except ValueError:
                print("Nota invalida. Ingrese un numero.")

    estudiante = {"nombre": nombre, "edad": edad, "notas": notas}
    lista_estudiantes.append(estudiante)
    print(f"Estudiante agregado exitosamente.")

    while True:
        agregar_otro = input("¿Desea agregar otro estudiante? (s/n): ").lower()
        if agregar_otro == "s":
            return agregar_estudiante()
        elif agregar_otro == "n":
            return
        else:
            print("Opcion invalida.")
            continue


def agregar_nota():
    while True:
        nombre = input("Ingrese el nombre del estudiante al que desea agregar una nota: ")
        if nombre.isdigit():
            print("Nombre invalido.")
            continue
        break

    encontrado = False
    for estudiante in lista_estudiantes:
        if estudiante["nombre"] == nombre:
            encontrado = True
            while True:
                try:
                    nueva_nota = float(input("Ingrese la nueva nota:"))
                    if 0 <= nueva_nota <= 100:
                        estudiante["notas"].append(nueva_nota)
                        print(f"Nota agregada exitosamente a {nombre}.")
                        break
                    else:
                        print("La nota debe estar entre 0 y 100.")
                except ValueError:
                    print("Nota invalida. Ingrese un numero.")
                    continue
            break

    if not encontrado:
        print("Estudiante no encontrado.")
        return

    while True:
        agregar_otra_nota = input("Desea agregar una nota a otro estudiante? (s/n): ")
        if agregar_otra_nota == "s":
            return agregar_nota()
        elif agregar_otra_nota == "n":
            return
        else:
            print("Opcion invalida.")
            continue


def editar_nota():
    while True:
        nombre = input("Ingrese el nombre del estudiante: ")
        if nombre.isdigit():
            print("Nombre invalido.")
            continue
        break

    for estudiante in lista_estudiantes:
        if estudiante["nombre"] == nombre:
            if not estudiante["notas"]:
                print(f"El estudiante {estudiante['nombre']} no tiene notas para editar.")
                return
            
            print(f"Notas actuales de {estudiante['nombre']} : {estudiante['notas']}")

            while True:
                try:
                    indice_nota = int(input("Ingrese el indice de la nota que desea editar (comenzando desde 0): "))
                    if 0 <= indice_nota < len(estudiante['notas']):
                        nueva_nota = float(input("Ingrese la nueva nota:"))
                        if 0 <= nueva_nota <= 100:
                            estudiante['notas'][indice_nota] = nueva_nota
                            print(f"Nota actualizada exitosamente.")
                            return
                        else:
                            print("La nueva nota debe estar entre 0 y 100.")
                except ValueError:
                    print("Valor invalido. Intente de nuevo")
                    continue

    print("Estudiante no encontrado.")

    editar_otra_nota = input("Desea editar una nota de otro estudiante? (s/n):" )
    if editar_otra_nota == "s":
        return editar_nota()
    elif editar_otra_nota == "n":
        return
    else:
        print("Opcion invalida.")
        return


def eliminar_nota():
    while True:
        nombre = input("Ingrese el nombre del estudiante:")
        if nombre.isdigit():
            print("Nombre invalido.")
            continue
        break

    for estudiante in lista_estudiantes:
        if estudiante["nombre"] == nombre:
            if not estudiante["notas"]:
                print(f"El estudiante {estudiante["nombre"]} no tiene notas para editar.")
                return
            
            print(f"Notas actuales de {estudiante["nombre"]} | {estudiante["notas"]}")

            while True:
                try:
                    indice_nota = int(input("Ingrese el indice de la nota que desea eliminar (comenzando desde 0): "))
                    if 0 <= indice_nota < len(estudiante["notas"]):
                        estudiante["notas"].pop(indice_nota)
                        print("Nota eliminada exitosamente.")
                        return
                    else:
                        print("Indice invalido.")
                except ValueError:
                    print("Valor invalido. Intente de nuevo.")
                    continue

    print("Estudiante no encontrado.")

    eliminar_otra_nota = input("Desea eliminar una nota de otro estudiante? (s/n):" )
    if eliminar_otra_nota == "s":
        return eliminar_nota()
    elif eliminar_otra_nota == "n":
        return
    else:
        print("Opcion invalida.")
        return


def calcular_promedio():
    while True:
        nombre = input("Ingrese el nombre del estudiante: ")
        if nombre.isdigit():
            print("Nombre invalido.")
            return
        break

    for estudiante in lista_estudiantes:
        if estudiante["nombre"] == nombre:
            if not estudiante["notas"]:
                print(f"El estudiante {estudiante["nombre"]} no tiene notas para calcular. ")
                return
            
            prmedio = sum(estudiante["notas"]) / len(estudiante["notas"]) 
            print(f"El promedio de notas de {estudiante["nombre"]} es: {prmedio:.2f}")
            return
        
    print("Estudiante no encontrado. ")

    calcular_otra_nota = input("Desea calcular una nota de otro estudiante? (s/n):" )
    if calcular_otra_nota == "s":
        return calcular_promedio()
    elif calcular_otra_nota == "n":
        return
    else:
        print("Opcion invalida.")
        return


def mostrar_estudiantes():
    if not lista_estudiantes:
        print("No hay estudiantes registrados.")
        return
    
    for estudiante in lista_estudiantes:
        print(f"Nombre: {estudiante["nombre"]} | Edad: {estudiante["edad"]} | Notas: {estudiante["notas"]}")

def menu():
    while True:
        try:
            menu_opcion = int(input(
            "1. Agregar estudiante\n" 
            "2. Mostrar estudiantes\n"
            "3. Agregar nota a estudiante\n" 
            "4. Editar nota de estudiante\n" 
            "5. Eliminar nota de estudiante\n" \
            "6. Calcular promedio de estudiante\n" 
            "7. Salir\n"
            ""))

            if menu_opcion == 1:
                agregar_estudiante()
            elif menu_opcion == 2:
                mostrar_estudiantes()
            elif menu_opcion == 3:
                agregar_nota()
            elif menu_opcion == 4:
                editar_nota()
            elif menu_opcion == 5:
                eliminar_nota()
            elif menu_opcion == 6:
                calcular_promedio()
            elif menu_opcion == 7:
                break
            else:
                print("Opcion invalida. Intente de nuevo.")
        except ValueError:
            print("Opcion invalida. Intente de nuevo.")

menu()

#26
productos = {
    "manzana" : 500 , "leche" : 2000 ,
    "pan" : 3000    , "naranja" : 500
}

carrito = []


while True:

    try:
        menu = int(input(
                    "1. Mostrar productos\n"
                    "2. Agregar producto\n"
                    "3. Eliminar producto\n"
                    "4. Ver carrito\n"
                    "5. Salir\n"
    ))
        
        if menu < 1 or menu > 5:
            print("Error, el menu es de 5 opciones")
            continue
    except ValueError:
        print("Ingrese un valor valido.")
        continue


    if menu == 1:
                for producto, precio in productos.items():
                    print(f"- {producto} : {precio}\n")
    elif menu == 2:
        newProduct = input("Ingrese el producto que desea agregar: ").lower()
        if newProduct in productos:
            carrito.append(newProduct)
            print(f"Se agregó {newProduct} al carrito.")
        else:
            print("Producto no disponible en la tienda.")
    elif menu == 3:
        remover_producto = input("Ingrese el producto que quiere eliminar: ")
        if remover_producto in carrito:
            carrito.remove(remover_producto)
            print(f"Se elimino {remover_producto} del carrito")
        else:
            print("El producto no esta en el carrito.")   
    elif menu == 4:
            if carrito:
                total = 0
                print("Productos en el carrito:")
                for item in carrito:
                    print(f"- {item} (${productos[item]})")  
                    total += productos[item]                 
                    print(f"Total: ${total}\n")
            else:
                print("El carrito está vacío.")

    elif menu == 5:
        print("Gracias por usar el carrito: ")
        break


#27
dinero_guardado = []

def agregar_dinero():

    while True:
        try:
            monto = float(input("Introduzca el monto de dinero: "))
            if monto <= 0:
                print("No ingresaste dinero.")
                continue
            break
        except ValueError:
            print("Ingrese un valor valido.")

    dinero = {"tipo" : "ingreso" ,"dinero" : monto}
    dinero_guardado.append(dinero)
    print("El dinero se ingreso correctamente.")


def mostrar_saldo():

    if not dinero_guardado:
        print("No tienes dinero en la cuenta")
        return

    total_monto = sum(item["dinero"] for item in dinero_guardado)
    print(f"Tu saldo total es: ${total_monto}")


def movimientos():
    if not dinero_guardado:
        print("No tienes movimientos en tu cuenta:")
        return

    total_monto = 0
    for i, elementos in enumerate(dinero_guardado, start=1):
        signo = "+" if elementos["dinero"] > 0 else "-"
        tipo = "ingreso" if elementos["dinero"] > 0 else "retiro"
        print(f"Movimiento {i}: {tipo} {signo}${abs(elementos['dinero']):.2f}")
        total_monto += elementos["dinero"]

    print(f"Saldo total actual: ${total_monto:.2f}\n0")

def retirar_monto():

    saldo_total = sum(item["dinero"] for item in dinero_guardado)

    if saldo_total <= 0:
        print("No tienes dinero en la cuenta")
        return
    
    while True:
        try:
            retirar_dinero = float(input("Ingrese cuanto desea retirar: "))
            if retirar_dinero < 0:
                print("Ingrese un monto válido mayor que cero.")
                continue
            if retirar_dinero > saldo_total:
                print(f"No tienes suficiente dinero. tu saldo es {saldo_total}")
                continue
            break
        except ValueError:
            print("Ingrese un valor valido.")

    dinero_guardado.append({"tipo": "retiro", "dinero": -retirar_dinero})
    print(f"Has retirado ${retirar_dinero:.2f} correctamente.\n")



def menu():
    while True:
        try:
            menu = int(input(
            "1. Agregar dinero\n" 
            "2. Mostrar saldo\n" 
            "3. Ver movimientos de cuenta\n" 
            "4. Retirar dinero\n" 
            "5. Salir\n" ))

            if menu == 1:
                agregar_dinero()
            elif menu == 2:
                mostrar_saldo()
            elif menu == 3:
                movimientos()
            elif menu == 4:
                retirar_monto()
            elif menu == 5:
                break
            else:
                print("Ingrese una opcion valida.\n")
        except ValueError:
            print("Ingrese una opcion valida.\n")


menu()

#28
estudiantes = []

def agregar_estudiantes():
    pedir_nombre = input("Ingrese el nombre del estudiante: ")
    if pedir_nombre.isdigit():
        print("El nombre no puede contener numeros. Intente de nuevo.")
        return agregar_estudiantes()
    
    while True:
        try:
            pedir_edad = int(input("Ingrese la edad del estudiante: "))
            if pedir_edad <= 0:
                print("Debe ingresar un numero mayor a 0. Intende de nuevo.")
                continue
            break
        except ValueError:
            print("Ingrese un valor valido.")
            continue

    while True:
        try:
            pedir_nota = float(input("Ingrese la nota del estudiante: "))
            if pedir_nota < 0 or pedir_nota > 100:
                print("La nota debe ser enntre 0 y 100. Intente de nuevo.")
                continue
            break
        except ValueError:
            print("Ingrese un valor valido.")
            continue
    
    estudiantes.append({
        "nombre": pedir_nombre,
        "edad": pedir_edad,
        "nota": pedir_nota
    })

    agregar_mas = input("¿Desea agregar otro estudiante? (s/n): ")
    if agregar_mas.lower() == "s":
        return agregar_estudiantes()
    else:
        print("Lista de estudiantes ingresados: ")
        for estudiante in estudiantes:
            print(f" Nombre: {estudiante["nombre"]} | Edad: {estudiante["edad"]} | Nota: {estudiante["nota"]}")

    
def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registradors.")
        return
    
    for estudiante in estudiantes:
        print(f" Nombre: {estudiante["nombre"]} | Edad: {estudiante["edad"]} | Nota: {estudiante["nota"]}")


def buscar_estudiante():
    buscar_est = input("Ingrese el nombre del estudiante: ")

    if buscar_est.isdigit():
        print("El nombre no puede contener numeros. Intente de nuevo.")
        return buscar_estudiante()
    
    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == buscar_est.lower():
            print(f" Nombre: {estudiante["nombre"]} | Edad: {estudiante["edad"]} | Nota: {estudiante["nota"]}")
            return
    
    print("Estudiante no encontrado.")


def eliminar_estudiante():
    eliminar_est = input("Ingrese el nombre del estudiante: ")
    if eliminar_est.isdigit():
        print("El nombre no puede contener números. Intente de nuevo.")
        return eliminar_estudiante()
    
    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == eliminar_est.lower():
            estudiantes.remove(estudiante)
            print(f"Estudiante {eliminar_est} eliminado.")

            agregar_otro = input("¿Desea eliminar otro estudiante? (s/n): ")
            if agregar_otro.lower() == "s":
                return eliminar_estudiante()
            else:
                return

    print("Estudiante no encontrado.")
    return eliminar_estudiante()


def menu():
    while True:
        menu = input(
            "1. Agregar estudiante\n"
            "2. Mostrar estudiantes\n"
            "3. Buscar estudiante\n"
            "4. Eliminar estudiantes\n"
            "5. Salir\n")
        
        try:
            if menu == "1":
                agregar_estudiantes()
            elif menu == "2":
                mostrar_estudiantes()
            elif menu == "3":
                buscar_estudiante()
            elif menu == "4":
                eliminar_estudiante()
            elif menu == "5":
                break
            else:
                print("Opcion no valida. intente de nuevo")
                continue
        except ValueError:
            print("Opcion no valida. Intente de nuevo.")
            return menu()

menu()            
        
#29
import math

def sumar():
    while True:
        try:
            numero1 = float(input("Ingrese un numero: "))
        except ValueError:
            print("Ingrese un valor valido.")
            continue
        break

    while True:    
        try:
            numero2 = float(input("Ingrese otro numero: "))
        except ValueError:
            print("Ingrese un valor valido.")
            continue
        break

    resultado = numero1 + numero2
    print(f"{numero1} + {numero2} = {resultado}")


def restar():
    while True:
        try:
            numero1 = float(input("Ingrese un numero: "))
        except ValueError:
            print("Ingrese un valor valido.")
            continue
        break

    while True:
        try:
            numero2 = float(input("Ingrese otro numero: "))
        except ValueError:
            print("Ingrese un valor valido.")
            continue
        break

    resultado = numero1 - numero2
    print(f"{numero1} - {numero2} = {resultado}")


def multiplicar():
    while True:
        try:
            numero1 = float(input("Ingrese un numero: "))
        except ValueError:
            print("Ingrese un valor valido.")
            continue
        break

    while True:
        try:
            numero2 = float(input("Ingrese otro numero: "))
        except ValueError:
            print("Ingrese un valor valido.")
            continue
        break

    resultado = numero1 * numero2
    print(f"{numero1} * {numero2} = {resultado}")


def dividir():
    while True:
        try:
            numero1 = float(input("Ingrese un numero: "))
        except ValueError:
            print("Ingrese un valor valido.")
            continue
        break

    while True:
        try:
            numero2 = float(input("Ingrese otro numero: "))
        except ValueError:
            print("Ingrese un valor valido.")
            continue
        break

    resultado = numero1 / numero2
    print(f"{numero1} / {numero2} = {resultado}")


def potencia():
    while True:
        try:
            numero1 = float(input("Ingrese un numero: "))
        except ValueError:
            print("Ingrese un valor valido.")
            continue
        break

    while True:
        try:
            numero2 = float(input("Ingrese otro numero: "))
        except ValueError:
            print("Ingrese un valor valido.")
            continue
        break

    resultado = numero1 ** numero2
    print(f"{numero1} ** {numero2} = {resultado}")


def potencia():
    while True:
        try:
            numero1 = float(input("Ingrese un numero: "))
        except ValueError:
            print("Ingrese un valor valido.")
            continue
        break

    while True:
        try:
            numero2 = float(input("Ingrese otro numero: "))
        except ValueError:
            print("Ingrese un valor valido.")
            continue
        break

    resultado = numero1 ** numero2
    print(f"{numero1} ** {numero2} = {resultado}")


def raiz_cuadrada():
    while True:
        try:
            numero = float(input("Ingrese un numero:"))
            if numero < 0 :
                print("Ingrese un numero mayor a cero.")
                continue

        except ValueError:
            print("Ingrese un valor valido.")
            continue
        break
    resultado = math.sqrt(numero)
    print(f"La raiz cuadrada de {numero} es {resultado}")


def factorial():
    while True:
        try:
            numero = int(input("Ingrese un numero: "))
            if numero < 0 :
                print("Ingrese un numero mayor a cero.")
                continue
        except ValueError:
            print("Ingrese un valor valido.")
            continue
        break
    resultado = math.factorial(numero)
    print(f"El factorial de {numero} es {resultado}")


def trigonometria():
    while True:
        try:
            angulo_grados = float(input("Ingrese un angulo en grado: "))
        except ValueError:
            print("Ingrese un valor valido.")
            continue
        break
    angulo_radianes = math.radians(angulo_grados)

    print(f"Seno de {angulo_grados}° = {math.sin(angulo_radianes)}")
    print(f"Coseno de {angulo_grados}° = {math.cos(angulo_radianes)}")
    print(f"Tangente de {angulo_grados}° = {math.tan(angulo_radianes)}")


def menu():
    while True:
        try:
            menu_opciones = input(
                "\nSeleccione una opcion:\n"
                "1. Sumar\n"
                "2. Restar\n"
                "3. Multiplicar\n"
                "4. Dividir\n"
                "5. Potencia\n"
                "6. Raiz Cuadrada\n"
                "7. Factorial\n"
                "8. Trigonometria\n"
                "9. Salir\n"
                "Ingrese el numero de la opcion deseada: "
            )
            if menu_opciones == "1":
                sumar()
            elif menu_opciones == "2":
                restar()
            elif menu_opciones == "3":
                multiplicar()
            elif menu_opciones == "4":
                dividir()
            elif menu_opciones == "5":
                potencia()
            elif menu_opciones == "6":
                raiz_cuadrada()
            elif menu_opciones == "7":
                factorial()
            elif menu_opciones == "8":
                trigonometria()
            elif menu_opciones == "9":
                break
            else:
                print("Ingrese una opcion valida")
        except ValueError:
            print("Ingrese una opcion valida")

menu()

#30
import re

lista_contactos = []

def agregar_contactos():

    while True:
        nombre_contacto = input("Ingrese el nombre: ").strip()
        if nombre_contacto.isdigit():
            print("Ingrese solo caracteres.")
            continue
        break

    while True:
            numero_contacto = input("ingrese el numero de telefono. (10 digitos): ")
            if re.fullmatch(r"\d{10}", numero_contacto):
                break
            print("Error. Debe contener 10 digitos.")

    lista_contactos.append({"nombre": nombre_contacto, "numero": numero_contacto})

    while True:
        agregar_otro = input("¿Desea agregar otro contacto? (s/n)").lower()
        if agregar_otro == "s":
            return agregar_contactos()
        elif agregar_otro == "n":
            break
        else:
            print("Ingrese una opcion valida.")
            
    print("\n--- Contactos agregados ---")
    for contactos in lista_contactos:
        print(f"Contacto agregado: Nombre: {contactos['nombre']} | Numero: {contactos['numero']} ")


def buscar_contacto():
    while True:
        nombre = input("Ingrese el nombre del contacto: ")
        if nombre.isdigit():
            print("Ingrese solo caracteres.")
            continue
        break

    encontrado = False

    for contacto in lista_contactos:
        if contacto["nombre"].lower() == nombre.lower():
            print(f"Nombre: {contacto['nombre']} | Numero: {contacto['numero']}")
            encontrado = True

    if not encontrado:
        print("Contacto no encontrado.")

    while True:
        buscar_otro = input("¿Desea buscar otro contacto? (s/n): ")
        if buscar_otro == "s":
            return buscar_contacto()
        elif buscar_otro == "n":
            return
        else:
            print("Ingrese un valor valido")


def eliminar_contacto():
    while True:
        nombre = input("Ingrese el nombre del contacto: ")
        if nombre.isdigit():
            print("Ingrese solo caracteres.")
            continue
        break

    encontrado = False

    for contacto in lista_contactos[:]:
        if contacto["nombre"].lower() == nombre.lower():
            lista_contactos.remove(contacto)
            print(f"Contacto {nombre} eliminado.")
            encontrado = True

    if not encontrado:
        print("contacto no encontrado.")

    while True:
        eliminar_otro = input("¿Desea eliminar otro contacto? (s/n): ").lower()
        if eliminar_otro == "s":
            return eliminar_contacto()
        elif eliminar_otro == "n":
            return
        else:
            print("Ingrese un valor valido. (s/n)")


def editar_contacto():

    while True:
        nombre = input("Ingrese el nombre del contacto: ")
        if nombre.isdigit():
            print("Ingrese solo caracteres.")
            continue
        break

    encontrado = False

    for contacto in lista_contactos:
        if contacto["nombre"].lower() == nombre.lower():
            while True:
                nuevo_numero = input("Ingrese el nuevo numero de telefono (10 digitos): ")
                if re.fullmatch(r"\d{10}", nuevo_numero):
                    contacto["numero"] = nuevo_numero
                    print(f"Contacto {nombre} actualizado. ")
                    encontrado = True
                    break
                else:
                    print("Error. Debe contener 10 digitos. ")
            break

    if not encontrado:
        print("Contacto no encontrado.")


def menu():
    while True:
        try:
            menu_opciones = int(input(
                "1. Agregar contacto\n"
                "2. Buscar contacto\n"
                "3. Eliminar contacto\n"
                "4. Editar contacto\n"
                "5. Salir\n"
            ))

            if menu_opciones == 1:
                agregar_contactos()
            elif menu_opciones == 2:
                buscar_contacto()
            elif menu_opciones == 3:
                eliminar_contacto()
            elif menu_opciones == 4:
                editar_contacto()
            elif menu_opciones == 5:
                break
            else:
                print("Ingrese una opcion valida.")
        except ValueError:
            print("Ingrese una opcion valida.")

menu()  