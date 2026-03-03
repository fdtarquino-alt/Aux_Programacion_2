class instrumento:
    def __init__(self,nombre:str,material:str,tipo:str):
        self.nombre = nombre
        self.material = material
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo:str):
        self.__tipo = tipo

    def __str__(self):
        return f"instrumento[nombre: {self.nombre}, material: {self.material}, tipo: {self.__tipo}]"


if __name__=="__main__":
    i1 = instrumento("guitarra","madera","cuerda")
    i2 = instrumento("trompeta","metal","aire")
    print(i1)
    print(i2)
    print("tipo de i1:", i1.get_tipo())
    i1.set_tipo("ELECTRICO")
    print("nuevo tipo de i1:", i1.get_tipo())
