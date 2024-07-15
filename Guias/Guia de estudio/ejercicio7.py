# a
estudiantes = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    carrera = input(f"Ingrese la carrera del estudiante {i+1}: ")
    nota1 = float(input(f"Ingrese la nota del primer laboratorio del estudiante {i+1}: "))
    nota2 = float(input(f"Ingrese la nota del segundo laboratorio del estudiante {i+1}: "))
   
    # b
    estudiantes[nombre] = (carrera, (nota1, nota2))

# c
for nombre, datos in estudiantes.items():
    carrera, notas = datos
    print(f"Estudiante: {nombre}")
    print(f"Carrera: {carrera}")
    print(f"Notas: {notas}")
    print("------")
