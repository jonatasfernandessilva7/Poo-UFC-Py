from Gerente import Gerente

if __name__ == '__main__':
	gerente = Gerente("joana", "123456009", 125.50, "mariajoana123", 2)
	print(vars(gerente))	
	print(f'novo salario: {gerente.getBonificacao()}')