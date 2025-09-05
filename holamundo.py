#se puede importar en otro archivo
def sayHello(name):
    print(f"Hola, {name}!")
    
#se ejecuta solo si se corre este archivo directamente
if __name__ == "__main__":
    print("Hola, Mundo!")
    sayHello("pepe")