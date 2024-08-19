print()

n = int(input("Ingrese la cantidad de cubos que desea calcular: "))

cubos = []
suma_impares = 0
siguiente_impar = 1


for i in range(1, n + 1):
    suma_actual = 0
    suma = []
    for a in range(i):
        suma.append(siguiente_impar)
        suma_actual += siguiente_impar
        siguiente_impar += 2
    
    cubos.append(suma_actual)
    
    suma_str = " + ".join([str(x) for x in suma])
    
    print(f"{i}³ = {suma_str} = {suma_actual}")

print()