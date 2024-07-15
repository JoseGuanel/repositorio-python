import random
"""5. Crear 20 numeros, que se encuentren en el intervarlo 40 al 350 y los almacene en una ´
lista y luego pida buscar algun numero dentro de los almacenados. Adem ´ as que muestre ´
la cantidad de ocurrencias de ese numero buscado. (Se permite el uso de la Biblioteca
Random)
"""""
lista=[]
for i in range(20):
    x= random.randint(40,350)
    lista.append(x)

print(lista)
a=int(input("Ingrese numero que desea buscar: "))
ocurrencia=0
for k in range(20):
    if lista[k]==a:
        ocurrencia+=1
print(f"El numero ingresado se ha encontrado {ocurrencia} veces.")