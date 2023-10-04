class Funcionario:
	def __init__(self, nome, cpf, salario):
		self.__nome = nome
		self.__cpf = cpf
		self.__salario = salario


	def getNome(self):
		return self.__nome

	def getCpf(self):
		return self.__cpf

	def getSalario(self):
		return self.__salario

	def setNome(self, nome):
		self.__nome = nome 

	def setCpf(self, cpf):
		self.__cpf = cpf 

	def setSalario(self, salario):
		self.__salario = salario

	def getBonificacao(self):
		return self.__salario * 0.10