#encapsulamento e herança 
'''
class Test1:
    a = 1 
    _b = 2 
    __c = 3 

class Test2(Test1):
    __d = 4
    def __init__(self):
        super().__init__()
        print(self.a)
        print(self._b) #erro
        print(self.__c) #erro
        print(self.__d) #erro

t1 = Test2()
'''

class Pessoa:
    def __init__(self, nome:str, sexo:str, cpf:str, ativo:bool):
        self.__nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.__ativo = ativo
    
    def getNome(self):
        return self.__nome

    def getAtivo(self):
        return self.__ativo

    def setNome(self, nome):
        self.__nome = nome
    
    def setAtivo(self, ativo):
        self.__ativo = ativo
    
    def verificaDesativar(self, sit):
        if(sit == False):
            print("desativado")
        else:
            print("ativo")

pessoa = Pessoa("joao", "masc", "40028922", True)
pessoa.verificaDesativar(False)
pessoa.setAtivo(True)
pessoa.verificaDesativar(pessoa.getAtivo())
pessoa.setNome("jose")
print(pessoa.getNome())