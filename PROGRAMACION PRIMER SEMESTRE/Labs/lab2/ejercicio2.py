#Ejercicio 2
#1.
resumen=str(input("Ingrese un resumen del articulo(igual o menor a 60 caracteres: "))
#2.
true_false=len(resumen)<=60
#3.
#a
print(f"La longitud de caracteres del resumen es de {len(resumen)}")
#b
resumen=resumen.upper()
#c
print(resumen[-10:])
