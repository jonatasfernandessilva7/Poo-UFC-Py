class Carro:
    def __init__(self, modelo:str, ano:int, cor:str, velocidade:int):
        self.__modelo = modelo
        self.__ano = ano
        self.__cor = cor
        self.__velocidade = velocidade
        print("carro criado")
        print(modelo,"\n",ano,"\n",cor)

    @property
    def carro(self):
        return self.__modelo

    @carro.setter
    def carro(self, modelo):
        self.__modelo = modelo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano
    
    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def ano(self, cor):
        self.__cor = cor

    @property
    def velocidade(self):
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, velo:int):
        self.__velocidade = velo

    def printModelo(self):
        print("sou o {}".format(self.__modelo))

    def criaPortas(self, portas:int):
        print("seu carro tem {} portas".format(portas))

    def acelerar(self):
        self.ligarFarois()
        print("acelerando vrum vrum")
        self.__velocidade += 1
        print("velocidade atual: {}".format(self.__velocidade))
        self.frear()

    def frear(self):
        parar = str(input("quer parar ? s= sim | n = nao -> "))
        if parar == 's':
            self.__velocidade = 0
            print("parado")
            print("velocidade atual: {}".format(self.__velocidade))
            self.desligarFarois()
            return parar
        self.acelerar()
        return parar
    
    def ligarFarois(self):
        print("farol ligado 🚨")

    def desligarFarois(self):
        print("farol desligado")