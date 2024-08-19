########## Reto2 
nombre= input("Ingresa el nombre del estudiante: ")
asignatura1={
    "nombre": nombre,
    "asignatura": input("Ingrese la asignatura: "),
    "nota1": float(input("Ingrese la nota de Laboratorio N°1: ")),
    "nota2": float(input("Ingrese la nota de Laboratorio N°2: ")),
    "nota3": float(input("Ingrese la nota de Laboratorio N°3: "))
}

asignatura2={
    "nombre": nombre,
    "asignatura": input("Ingrese la asignatura: "),
    "nota1": float(input("Ingrese la nota de Laboratorio N°1: ")),
    "nota2": float(input("Ingrese la nota de Laboratorio N°2: ")),
    "nota3": float(input("Ingrese la nota de Laboratorio N°3: "))
}

asignatura3={
    "nombre": nombre,
    "asignatura": input("Ingrese la asignatura: "),
    "nota1": float(input("Ingrese la nota de Laboratorio N°1: ")),
    "nota2": float(input("Ingrese la nota de Laboratorio N°2: ")),
    "nota3": float(input("Ingrese la nota de Laboratorio N°3: "))
}



consultar_estudiante={
    nombre: [(asignatura1["asignatura"], {asignatura1["nota1"], asignatura1["nota2"], asignatura1["nota3"]}, 
              round((asignatura1["nota1"]*0.30) + (asignatura1["nota2"]*0.50) + (asignatura1["nota3"]*0.20),1 )) , 
              
              (asignatura2["asignatura"], {asignatura2["nota1"], asignatura2["nota2"], asignatura2["nota3"]}, 
              round((asignatura2["nota1"]*0.30) + (asignatura2["nota2"]*0.50) + (asignatura2["nota3"]*0.20),1 )),
              
              (asignatura3["asignatura"], {asignatura3["nota1"], asignatura3["nota2"], asignatura3["nota3"]}, 
              round((asignatura3["nota1"]*0.30) + (asignatura3["nota2"]*0.50) + (asignatura3["nota3"]*0.20),1 ))]

}

print(consultar_estudiante[nombre])