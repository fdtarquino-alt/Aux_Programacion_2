class anime:
    def __init__(self,nombre:str,genero:str,nro_episodios:int):  
        self.nombre=nombre
        self.genero=genero
        self.__nro_episodios=nro_episodios
        self.__episodios=[]
    def __str__(self):
        return f"anime:{self.nombre},genero:{self.genero},episodios:{self.__nro_episodios}"
if __name__=="__main__":
    a1=anime("naruto","accion",220)
    a2=anime("one piece","aventura", 1000)
    print(a1)
    print(a2)
    

        