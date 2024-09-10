print("Introduccion a clases")
class Animal:
    edad = 3
    raza = "chihuahua"
    def Come():
        lacomida = "Croquetas"
        return lacomida
print("Creando el objeto de la clase animal")
perro=Animal()
print(f"Edad del perro: {perro.edad}")
print(f"Raza del perro: {perro.raza}")
print(f"El perro come: {Animal.Come()}")