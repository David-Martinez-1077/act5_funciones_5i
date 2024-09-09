print("Manejo de funciones V1")

def hola_mundo():
    print("Hola aquí estoy dentro de la función")

def Mensa(msg):
    print(msg)
    

def EscribeNC(Nombre, Apellido):
    print(Nombre, Apellido)
    print(f"Tu nombre completo es: {Nombre} {Apellido}")


def suma2numeros(n1, n2):
    s=n1 + n2
    return f"la suma es {n1} + {n2} es: {s}"


# Llamando a la función 
hola_mundo()

Mensa("Hola Whatsapp") # llama a la mensa con un parametro 
Mensa("El profe me sorprendió enviando mensajes") # llama a la mensa con un parametro
EscribeNC("David", "Martínez")
print("Funciones que regresan valores")
print(suma2numeros(7, 3))
print(suma2numeros(15, 45))


