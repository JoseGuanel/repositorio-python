# Ejercicio Propuesto_1
"""Joel"""

n1_joel=float(input("Ingrese la primera nota de Joel: "))
n2_joel=float(input("Ingrese la segunda nota de Joel: "))
n3_joel=float(input("Ingrese la tercera nota de Joel: "))

""""Alondra"""

n1_alondra=float(input("Ingrese la primera nota de Alondra: "))
n2_alondra=float(input("Ingrese la segunda nota de Alondra: "))
n3_alondra=float(input("Ingrese la tercera nota de Alondra: "))

"""Paz"""

n1_paz=float(input("Ingrese la primera nota de Paz: "))
n2_paz=float(input("Ingrese la segunda nota de Paz: "))
n3_paz=float(input("Ingrese la tercera nota de Paz: "))

prom_joel= (n1_joel + n2_joel + n3_joel)/3
prom_alondra= (n1_alondra + n2_alondra + n3_alondra)/3
prom_paz= (n1_paz + n2_paz + n3_paz)

print("----------------------------------------------")

#Promedios redondeados a 3 decimales
print("El promedio de Joel es de: ", round(prom_joel, 3))
print("El promedio de Alondra es de: ", round(prom_alondra, 3))
print("El promedio de Paz es de: ", round(prom_paz, 3))

print("----------------------------------------------")

#Nota minima de cada estudiante
print("La nota minima de Joel es: ", min(n1_joel,n2_joel,n3_joel))
print("La nota minima de Alondra es: ", min(n1_alondra, n2_alondra, n3_alondra))
print("La nota minima de Paz es: ", min(n1_paz, n2_paz, n3_paz))

print("----------------------------------------------")

#Promedio general de los estudiantes
print("El promedio general de los estudiantes es: ", (prom_joel + prom_alondra + prom_paz)/3)