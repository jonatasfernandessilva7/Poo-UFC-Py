class Carro:
    __modelo = None
    __ano = None
    __cor = None

    def __init__(self, modelo, ano, cor):
        self.__modelo = modelo
        self.__ano = ano
        self.__cor = cor
        print("carro criado")
        print(modelo,"\n",ano,"\n",cor)

    @property
    def carro(self):
        return self.__modelo

    @carro.setter
    def carro(self, modelo):
        self.__modelo = modelo

    def printModelo(self):
        print("sou o {}".format(self.__modelo))

    def criaPortas(self, portas:int):
        print("seu carro tem {} portas".format(portas))

