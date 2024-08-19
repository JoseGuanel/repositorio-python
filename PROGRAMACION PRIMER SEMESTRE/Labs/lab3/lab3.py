#Lab 3
### 
## a)
l_r={
    "nombre region": "los rios",
    "superficie": 18429,
    "habitantes": 404432
}

mag= {
    "nombre region": "magallanes",
    "superficie": 1382291,
    "habitantes":166533
}
censo_2017={
    "14": l_r,
    "12": mag
}
print(censo_2017) ###  


####Se agrega densidad a los sub-diccionarios ### 
### b)
l_r.update(
    {"densidad" :  round(l_r["habitantes"]/l_r["superficie"], 1)
    }
)

mag.update(
    {"densidad" :  round(mag["habitantes"]/mag["superficie"], 1)
    }
)

### Se agrega clave "Capital"
## c)
l_r.update(
    {
        "capital": "valdivia"
    }
)

mag.update(
    {
        "capital": "punta arenas"
    }
)

### Se agrega clave "Comunas"
## d)
l_r.update(
    {
        "comunas": ["Río Bueno", "La Unión", "Paillaco"]
    }
)
mag.update(
    {
        "comunas": ["Cabo de Hornos", "Puerto Williams", "Porvenir"]
    }
)

### Se agrega clave "Provincias"
## e)
l_r.update(
    {
        "provincias": ("Ranco", "Valdivia")
    }
)
mag.update(
    {
        "provincias": ("Antártica Chilena", "Magallanes", "Tierra del Fuego", "Última Esperanza")
    }
)

### Se actualiza la clave "nombre region" de magallanes
## f)
mag.update(
    {
        "nombre region": "Magallanes y Ántartica Chilena"
    }
)

### Imprimir cambios realizados
## g)
print(censo_2017)

### Obtener lista de tuplas con la clave y valor de cada elemento del diccionario
## h)
print("-----------------------------------------------")
lista=[]
for clave in censo_2017:
    x= (clave, censo_2017[clave])
    lista.append(x)
print("La lista es: ", lista)