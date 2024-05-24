#ejercicio 3
######### DATOS DEL PRIMER PRODUCTO #########
prod1=str(input("Ingresa la descripcion del primer producto (almenos 40 caracteres): "))
while len(prod1)<40:
    prod1=str(input("Haz ingresado menos de 40 caracteres!, Ingresa la descripción del primer producto: "))
clp_1=int(input("Ingrese el valor en CLP del primer producto: "))
stock_1=int(input("Ingrese la cantidad disponible del primer producto: "))

######### DATOS DEL SEGUNDO PRODUCTO #########

prod2=str(input("Ingresa la descripcion del segundo producto (almenos 40 caracteres): "))
while len(prod2)<40:
    prod2=str(input("Haz ingresado menos de 40 caracteres!, Ingresa la descripción del segundo producto: "))
clp_2=int(input("Ingrese el valor en CLP del segundo producto: "))
stock_2=int(input("Ingrese la cantidad disponible del segundo producto: "))

######### C. #########
#a.
prod1= prod1.upper()
prod2= prod2.upper()

#b.
u_prod= prod1 + " " + prod2
print(u_prod)
#c.
valortotal_1= clp_1 * stock_1
valortotal_2= clp_2 * stock_2

#d.

print("El valor total de todos los productos es: $", valortotal_1 + valortotal_2)
print("El precio promedio entre los productos es: $", (valortotal_1+valortotal_2)/2)


#easy