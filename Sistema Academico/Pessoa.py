class Pessoa:

    def _init_(self, nome:str, email:str, matricula:str):
        self.__nome = nome
        self.__email = email
        self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome
    
    @property
    def email(self):
        return self.__email
    
    @property
    def matricula(self):
        return self.__matricula
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @email.setter
    def nome(self, email):
        self.__email = email

    @matricula.setter
    def nome(self, matricula):
        self.__matricula = matricula
