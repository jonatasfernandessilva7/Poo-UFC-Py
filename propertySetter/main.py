from casa import Casa

if __name__ == '__main__':
    casa = Casa(12.50)
    print(casa.preco)
    casa.preco = 20.50
    print(casa.preco)