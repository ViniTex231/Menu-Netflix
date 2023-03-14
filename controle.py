# Classes

class ControleRemoto:
    def __init__(self, valorCor, altura, prof, largura):
        self.cor = valorCor
        self.altura = altura
        self.profundidade = prof
        self.largura = largura

    def passar_canal(self, botao):
        if botao == '+':
            print('Próximo canal')
        elif botao == '-':
            print('Canal anterior')

