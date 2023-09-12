from Triangulo import Triangulo

ladosDoUsuario = []
soma = 0
i = 3
for i in range(3):
    lado = float(input("digite um lado para o triangulo: "))
    ladosDoUsuario.append(lado)
    soma += ladosDoUsuario[i]

triangulo = Triangulo(ladosDoUsuario)
triangulo.printaPerimetro(soma)
triangulo.verificaMaiorValor(ladosDoUsuario)