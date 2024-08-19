### IF ELSE
edad=69
if edad >=18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

### elif 
if edad >= 18 and edad < 65:
    print("Eres mayor de edad.")
elif edad >= 65:
    print("Eres adulto mayor.")
else:
    print("Eres menor de edad.")


# WHILE

## While (condicion):
    #Pasara esto
dinero=2000
while dinero>1000:
    print("Aun tengo mas de mil pesos!", "-100 pesos")
    dinero-= 100

print(f"Me quedaron {dinero} pesos")
booleano=True

while booleano:
    print("Se repetira hasta que haya un break o cambie el booleano")
    if dinero > 1300:
        booleano= False
    else:
        print("+100 pesos")
        dinero +=100

