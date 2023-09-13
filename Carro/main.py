from Carro import  Carro

corolla = Carro("corolla", 2023, "azul", 0)
corolla.printModelo()
fusca = Carro("fusca", 1870, "verde", 0)
fusca.criaPortas(7)
fusca.acelerar()
fusca.velocidade = 78
print(fusca.velocidade)