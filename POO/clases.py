#APUNTES CLASE 19-08

class Guerrero():
    vida=225

class Mago():
    vida=150

class Cazador():
    vida=180

class Personaje():

    def __init__(self, name, clase):
        self.name = name
        self.clase = clase
        

    #Metodos
    def hablar(self):
        print(f"{self.name} esta hablando")
    def caminar(self):
        print(f"{self.name} esta caminando")




#Creacion de un objeto de la clase Personaje

jugador=Personaje(input("Ingrese nombre de jugador"), "Guerrero")

#Acceder a los atributos y metodos del objeto

print(f"{jugador.name} ")
print(f"La clase actual: {jugador.clase}")

jugador.hablar()
jugador.caminar()