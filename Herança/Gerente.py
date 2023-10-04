from Funcionario import Funcionario

informacoes = []

class Gerente(Funcionario):
	def __init__(self, nome, cpf, salario, senha, qtd_funcionarios):
		super().__init__(nome, cpf, salario)
		self.__senha = senha
		self._qtd_funcionarios = qtd_funcionarios

	def getSenha(self):
		return self.__senha

	def getQtd_funcionarios(self):
		return self._qtd_funcionarios

	def getBonificacao(self):
		return super().getBonificacao() + 1000

	def getFuncionarios(self):
		return self._funcionarios

	def setSenha(self, senha):
		self.__senha = senha

	def setQtd_funcionarios(self, qtd_funcionarios):
		self._qtd_funcionarios = qtd_funcionarios