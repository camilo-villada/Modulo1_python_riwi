#Nivel 4 Listas y Colecciones.

#19. Crear lista de frutas
frutas = ["manzana", "naranja", "pera", "sandia", "banano"]

#20. Agregar y eliminar elementos de la lista
frutas.append("mandarina")
print(frutas)

frutas.remove("manzana")
print(frutas)

#21. Buscar elemento
print(frutas[1])

#22. Lista de números y promedio.
numeros = [10, 20 ,30, 40, 50]

promedio = sum(numeros) / len(numeros)

print(promedio)

#23. Números pares: guardar solo los pares.
nums = [1,2,3,4,5,6,7,8,9,10]

for n in nums:
    if n % 2 == 0:
        print(n)

#24.
numss = [1,1,2,2,3,3,4,4,5,5]

nums1 = list(set(numss))
print(nums1)
