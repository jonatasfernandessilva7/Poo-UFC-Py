class Casa:

    def __init__(self, preco:float):
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, preco):
        if preco > 0 and isinstance(preco, float):
            self.__preco = preco
        else:
            print("grrr")