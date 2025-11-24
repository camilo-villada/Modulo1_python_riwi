#Nivel 3 bucles y repeticion.

#13.
for i in range(1, 11):
    print(i)

#14.
numero_n = int(input("Ingrese un numero: "))
suma = 0

for i in range(1, numero_n +1):
    suma = suma + i
    print(suma)

#15.
dato = int(input("Ingrese el primer valor: "))

for i in range(1, dato):
    print(f"{dato} x {i} = {dato * i}")

#16.
contador = int(input("Ingrese un dato para la cuenta regresiva: "))

while contador >= 0:
    print(contador)
    contador -= 1

#17.
import random

numero_aleatorio = random.randint(1, 5)
usuario = int(input("Adivina el numero: "))

while numero_aleatorio != usuario:
    print("No adivinaste")
    usuario = int(input("Adivina el numero de nuevo: "))

print("Adivinaste")

suma = 0
usu = int(input("Ingrese un numero: "))


while usu != 0:
   suma += usu
   usu = int(input("Ingrese otro numero: "))

print("la suma total es: ", suma)