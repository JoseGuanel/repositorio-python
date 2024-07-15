#Funciones
def promedio(x,y,z): #Aca esta la funcion que llamaste en tu codigo de abajo y los valores enviados a b c, toman como valor x y z respectivamente.
    prom= x+y+z
    prom= prom/3
    return prom   #Return significa retornar, lo que enviara el valor que este al lado de return al codigo exactamente donde llamaste a la funcion.



#Saludo
def saludo(x):
    print(f"Hola {x}, Bienvenido al juego.")



a=int(input("Ingresa un numero: "))
b=int(input("Ingresa un numero: "))
c=int(input("Ingresa un numero: "))

print(f"El promedio de los numeros ingresados es: {promedio(a,b,c)}") #Aca llamas a la funcion enviando los valores a b c

nombre=str(input("Ingresa tu nombre de usuario: "))
saludo(nombre)
