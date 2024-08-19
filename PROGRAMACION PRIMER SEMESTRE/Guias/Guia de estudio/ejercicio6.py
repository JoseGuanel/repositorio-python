# a
palabras_claves = []
print("Ingrese 5 palabras claves:")

for i in range(5):
    palabra = input(f"Palabra {i+1}: ")
    palabras_claves.append(palabra)

# b
palabras_unicas = list(set(palabras_claves))

# c
print("Lista original de palabras claves:", palabras_claves)
print("Lista sin duplicados:", palabras_unicas)
