#Nivel 1 fundamentos y variables.

#1.
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")

print(f"Hola {nombre}, tienes {edad} años")

#2.
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))

resultado = a + b
print("la suma de los numeros es: ", resultado)

#3.
base = float(input("Ingresa la base del triangulo: "))
altura = float(input("Ingresa la altura del triangulo: "))

area = (base * altura) / 2

print("El area del triangulo es:", area)

#4.
c = float(input("Ingrese la temperatura en Celsius: "))

f = (c * 1.8) + 32

print("La tempera tura en Farenheit es:", f)

#5.
variable1 = 10
variable2 = 10.0
variable3 = "hola mundo"
variable4 = True

print(type(variable1))
print(type(variable2))
print(type(variable3))
print(type(variable4))

#6.
edad_actual = int(input("Ingresa tu edad: "))

futuro = edad_actual + 10

print(f"En 10 años tendras {futuro} años de edad.")