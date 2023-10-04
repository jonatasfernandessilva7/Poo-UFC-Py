class Animal():
	def __init__(self, nome, especie, habitat, raca, idade, tipo_alimentacao, tipo_reproducao):
		self._nome = nome
		self._especie = especie
		self._habitat = habitat
		self._raca = raca 
		self._idade = idade
		self._tipo_alimentacao = tipo_alimentacao
		self._tipo_reproducao = tipo_reproducao

	def getNome(self):
		return self._nome

	def setNome(self, nome):
		self._nome = nome

class Ave(Animal):
	def __init__(self, nome, especie, habitat, raca, idade, tipo_alimentacao, tipo_reproducao, voa, tamanho_bico):
		super().__init__(nome, especie, habitat, raca, idade, tipo_alimentacao, tipo_reproducao)
		self._voa = voa 
		self._tamanho_bico = tamanho_bico