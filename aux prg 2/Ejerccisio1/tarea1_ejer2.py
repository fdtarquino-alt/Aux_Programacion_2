class televisor:
    def __init__(self,marca="desconocida",resolucion=1080,tipo="lcd"):
        self.__marca=marca
        self.__resolucion=resolucion
        self.__tipo=tipo
        def __str__(self):
            return f"televisor [marca: {self.__marca}, resolucion:{self.__resolucion}p, tipo: {self.__tipo}]"
        if __name__== "__main__": 
            t1=televisor("samsung",2160,"oled")
            t2=televisor()
            print(t1)
            print(t2)