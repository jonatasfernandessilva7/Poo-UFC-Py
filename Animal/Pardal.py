from Interface_e_Pais import Ave

class Pardal(Ave):
	def __init__(self, nome, especie, habitat, raca, idade, tipo_alimentacao, tipo_reproducao, voa, tamanho_bico, som):
		super().__init__(nome, especie, habitat, raca, idade, tipo_alimentacao, tipo_reproducao, voa, tamanho_bico)
		self.som = som