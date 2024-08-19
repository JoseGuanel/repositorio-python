"""Un negocio quiere organizar sus productos por fecha de vencimiento. Desarrollar un
programa que permita ingresar las fechas de vencimiento (día, mes, año) de tres productos
y almacenarlas en tuplas. Luego, mostrar las fechas ordenadas de menor a mayor.
a. Ingresar las fechas de vencimiento (día, mes, año) de tres productos por consola, y
almacenarlas en tuplas.
b. Ordenar las fechas de menor a mayor utilizando la función correspondiente de
Python.
c. Mostrar las fechas ordenadas."""


print("Fecha de vencimiento 1")
fecha1=int(input("Ingresa el dia de vencimiento: ")), int(input("Ingresa el mes de vencimiento: ")), int(input("Ingresa el año de vencimiento: "))
print("Fecha de vencimiento 2")
fecha2=int(input("Ingresa el dia de vencimiento: ")), int(input("Ingresa el mes de vencimiento: ")), int(input("Ingresa el año de vencimiento: "))
print("Fecha de vencimiento 3")
fecha3=int(input("Ingresa el dia de vencimiento: ")), int(input("Ingresa el mes de vencimiento: ")), int(input("Ingresa el año de vencimiento: "))
 
hola=sorted([fecha1, fecha2, fecha3])
print(hola)