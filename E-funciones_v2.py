print("Funciones creadas por el usuario")
#las funciones 
def Mi_lista():
    print("--Mi listas--")
    amigos = ["Homero", "Paty", "Lety"]
    for amigo in amigos:
        print(amigo)

    print("---------------------------------\n")

def mi_tupla():
    print("--Mi tupla--")
    pesos= ("mexicano", "Venezolano", "argentino")
    for amigo in pesos:
        print(amigo)
    print("---------------------------------\n")
    


def mi_diccionario():
    print("--Mi diccionario--")

    tienda= {"nombre": "Platanos", "precio": 30, "cantidad": 100}
    for key, value in tienda.items():
        print(f"{key}: {value}")
    print("---------------------------------\n")
    

def mi_conjunto():
    print("--Mi conjunto--")

    nombres = {"Pedro", "Anna", "Esperanza"}
    for nombre in nombres:
        print(nombre)
# llamadas a funciones
Mi_lista()
mi_tupla()
mi_diccionario()
mi_conjunto()