#listas
list1= ["Python", "Java", "C++"] 
print(list1)

list1.append("Rubi")
print(list1)

list1.remove("Java")
print(list1)

listnum= list(range(1,11)) #lista con numeros del 1 al 10
print(listnum)

#Listas pueden tener diferentes tipos de variables


listrandom= [2100, "Numeros", True, False, 2.102, (2,10)]
print(listrandom)

####TUPLAS
musica=tuple()
generos=("Rock","Metal", "Pop", "Rap")
print(type(generos))
tuplita=("José", 20, "Universidad", True)
print("La variable tuplita es de tipo: ", type(tuplita))
tuplita=list(tuplita)
print("La variable tuplita ahora es de tipo: ", type(tuplita))

#Diccionario
yo= {
    "Nombre": "José",
    "Edad": "20",
    "Ciudad": "Castro"
}
print(yo)
yo.pop("Edad") #### Elimina Edad: 20
print(yo) ####Diccionario modificado

#Actualizar diccionarios

yo.update({
    "Ciudad": "Santiago",
    "Edad": "21"
})
print(yo)