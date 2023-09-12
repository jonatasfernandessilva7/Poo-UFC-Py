class Triangulo:
    def __init__(self, lados:list):
        self.lados = lados

    def printaPerimetro(self, soma):
        print("o perimetro eh: {}".format(soma))

    def verificaMaiorValor(self, ladosDoUsuario):
        print("o maior valor eh: {}".format(max(ladosDoUsuario)))