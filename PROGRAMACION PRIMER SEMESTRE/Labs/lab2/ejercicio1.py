##### Ejercicio 1
#1.
#Precios
Manzana= 100
Pera= 250
Durazno= 300
#Cantidades a comprar
can_m=150
can_p=80
can_d=120
#2.
#Precio total cada fruta
precio_m=Manzana*can_m
print(f"El precio a pagar por las manzanas es de ${precio_m}")
precio_p=Pera*can_p
print(f"El precio a pagar por las peras es de ${precio_p}")
precio_d=Durazno*can_d
print(f"El precio a pagar por los duraznos es ${precio_d}")

#3.a
print(f"La suma a pagar por las manzanas y peras es de ${precio_m+precio_p}")
print(f"Valor maximo a pagar entre las 3 frutas es de ${max(precio_d,precio_m,precio_p)}")
print(f"Valor minimo a pagar entre las 3 frutas es de ${min(precio_d,precio_m,precio_p)}")
print(f"El promedio del precio unitario de todas las frutas es de ${(Manzana+Pera+Durazno)/3}")
