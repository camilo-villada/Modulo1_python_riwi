#Nivel 2 condicionales.

#7.
edad = int(input("Ingrese su edad: "))

if edad < 18:
    print("Eres menor de edad: ")
else:
    print("Eres mayor de edad")

#8.
n = int(input("Ingrese un numero: "))

if n < 0:
    print("El numero es negativo.")
elif n == 0:
    print("El numero es 0.")
else:
    print("El numero es positivo.")

#9.
numero = int(input("Ingrese un numero: "))

if numero % 2 == 0:
    print("Par.")
else:
    print("Impar.")

#10.
num = float(input("Ingrese el primer numero: "))
operacion = input("Ingrese la operacion (+, -, /, *): ")
num2 = float(input("Ingrese el segundo numero: "))

if operacion == "+":
    resultado = num + num2
elif operacion == "-":
    resultado = num - num2
elif operacion == "/":
    resultado = num / num2
elif operacion == "*":
    resultado = num * num2
else:
    print("Operacion no valida.")

print(f"{num} {operacion} {num2} = {resultado} ")

#11.
nota = float(input("Ingresa una nota de 0 a 100: "))

if nota >= 90:
    print("Excelente.")
elif nota >= 70:
    print("Aprobado.")
else:
    print("Reprobado.")

#12.
N_n1 = int(input("Ingrese el primero numero: "))
N_n2 = int(input("Ingrese el segundo numero: "))
N_n3 = int(input("Ingrese el tercer numero:" ))

if N_n1 > N_n2 and N_n1 > N_n3:
    print("Mayor", N_n1)
elif N_n2 > N_n1 and N_n2 > N_n3:
    print("Mayor", N_n2)
else:
    print("Mayor", N_n3)
    
if N_n1 < N_n2 and N_n1 < N_n3:
    print("Menor", N_n1)
elif N_n2 < N_n1 and N_n2 < N_n3:
    print("Menor", N_n2)
else:
    print("Menor", N_n3)    