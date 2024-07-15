#Numeros
estatura= 1.80 #float
peso= 70 #int

imc= peso / (estatura**2)
print(f"Mi imc es de {imc}")

#Strings
universidad= "Universidad de Los lagos"
asignatura= "Matematicas"
descripcion="Asignatura de introduccion a matematicas de primer semestre"
#imprimir un caracter del string segun la posicion indicada
print(universidad[0]) #primera letra 
print(universidad[1]) #segunda letra
print(universidad[2]) #tercera letra

#concatenacion
print(universidad + asignatura + descripcion)

#Multiplicar el texto por un numero
print("hola" * 4)
print(universidad.split()) #separa cada palabra de la variabe



#Booleanos
verdad= True
mentira= False

print(verdad, mentira)
print(1 == 0)


print()
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