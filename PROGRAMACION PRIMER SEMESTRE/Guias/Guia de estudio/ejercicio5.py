print("Debera ingresar 3 ciudades junto a su respectiva latitud y longitud")

c1 = input("\nIngrese la primera ciudad: ")
c1l = float(input("Ingrese la latitud(y): "))
c1lo = float(input("Ingrese la longitud(x): "))
co = (c1l,c1lo)

print(f"La primera ciudad {c1} tiene la latitud {c1l} y su longitud es {c1lo}")
print(f"Sus coordenadas (x,y) son {(co)}")

c2 = input("\nIngrese la segunda ciudad: ")
c2l = float(input("Ingrese la latitud(y): "))
c2lo = float(input("Ingrese la longitud(x): "))
co2 = (c2l,c2lo)

print(f"La segunda ciudad {c2} tiene la latitud {c2l} y su longitud es {c2lo}")
print(f"Sus coordenadas (x,y) son {int(co2)}")

c3 = input("\nIngrese la tercera ciudad: ")
c3l = float(input("Ingrese la latitud(y): "))
c3lo = float(input("Ingrese la longitud(x): "))
co3 = (c3l,c3lo)

print(f"La tercera ciudad {c3} tiene la latitud {c3l} y su longitud es {c3lo}")
print(f"Sus coordenadas (x,y) son {int(co3)}")

l1 = [c1, c2, c3]
t1 = {co, co2,co3}
