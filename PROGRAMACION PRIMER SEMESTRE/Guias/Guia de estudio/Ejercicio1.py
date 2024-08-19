""" Crear un programa que permita ingresar 4 marcas de bebidas gaseosas y almacenarlas en
una lista. Luego, mostrar la lista completa y el nombre de la primera y última bebida.
a. Ingresar 4 nombres de marcas de bebida por consola y almacenarlos en una lista.
b. Imprimir la lista completa.
c. Mostrar el primer y último nombre de las bebidas de la lista.
"""

bebida1=str(input("Ingresa la primera marca de bebida: "))
bebida2=str(input("Ingresa la segunda marca de bebida: "))
bebida3=str(input("Ingresa la tercera marca de bebida: "))
bebida4=str(input("Ingresa la cuarta marca de bebida: "))

lista=[bebida1,bebida2,bebida3,bebida4]
print(lista)
print(f"La primera bebida de la lista es {lista[0]} y ultima bebida de la lista {lista[3]}")
