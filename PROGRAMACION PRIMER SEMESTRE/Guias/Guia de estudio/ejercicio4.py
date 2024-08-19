print("Se le solicitara ingresas 3 nombres y sus edades")
di1 = dict(
    nombre = input("\nIngrese el primer nomnbre: "),
    edad = input("Ahora ingrese su edad: "),
    nombre2 = input("\nIngrese el segundo nomnbre: "),
    edad2 = input("Ahora ingrese su edad: "),
    nombre3 = input("\nIngrese el tercer nomnbre: "),
    edad3 = input("Ahora ingrese su edad: ")
)
print(di1.values())
di1.pop("nombre")
di1.pop("edad")
print(di1.values())
di1.update(
    nombre4= input("Ingresa otro nombre: "),
    edad4= int(input("Ingresa edad: "))
)
print(di1)
