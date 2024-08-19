print()

# Párrafo
parrafo = "La Universidad de los Lagos es una institución estatal fundada en 1993. Esta universidad regional entrega una contribución significativa al desarrollo sostenible del territorio. Como Universidad sus pilares fundamentales se basan en la inclusión, pluralismo, conciencia ambiental y participación democrática."
parrafo_m = parrafo.lower()
parrafo_dividido = parrafo_m.split()

# Palabra
palabra_buscada = "universidad"

# Numero de veces
contar = 0
veces_encontrada = []


for palabra in parrafo_dividido:
    if palabra == palabra_buscada:
        contar += 1
        veces_encontrada.append(palabra)


# Tupla
veces_encontrada = tuple(veces_encontrada)



print("La palabra", palabra_buscada, "aparece", contar, "veces")

print()