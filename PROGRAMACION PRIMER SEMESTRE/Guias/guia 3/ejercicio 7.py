n=int(input("Ingrese n para encontrar su factorial: "))
factorial= 1
if n==0:
    print("El factorial es 1")
else:
    for i in range(1,n+1):
        factorial= factorial*i
    print(f"El factorial de {n} es {factorial}")

