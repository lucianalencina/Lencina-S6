def saludar(nombre):
    print("Hola", nombre)
    print("¿Como estas?")
    print("Un gusto conocerte")

saludar("Solcho")
saludar("Vir")
saludar("Julian")
def saludar (nombre, estado):
    print("Hola " + nombre)
    print("¿Como estas? bien/mal")
    if estado=="bien":
        print("Que bueno que estes bien. ¿En que te puedo ayudar?")
    else:
        print("En que te puedo ayudar")
saludar(input("Escribe tu nombre:"), input("Escribe tu estado: (bien/mal)"))

def saludar(nombre, apellido, empresa):
    print("Hola " + nombre + apellido)
    print("Bienvenido a", empresa)
    print("Un gusto tenerte con nosotros")
saludar(nombre="Solcho ", apellido="Lopez", empresa="Google")
 