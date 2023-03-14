
class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.planos = ['basic', 'medium', 'premium']
        if plano in self.planos:
            self.plano = plano
        else:
            self.plano = ''
            print('Plano invalido')

    def mudar_plano(self, novo_plano):
        if novo_plano in self.planos:
            self.plano = novo_plano
        else:
            print('Plano invalido')

    def ver_filme(self, filme, plano_filme):
        if self.plano == 'premium':
            print(f'O cliente {self.nome} pode assistir o filme {filme}')
        elif self.plano == plano_filme:
            print(f'O cliente {self.nome} pode assistir o filme {filme}')
        elif self.plano == 'medium' and plano_filme == 'basic':
            print(f'O cliente {self.nome} pode assistir o filme {filme}')
        else:
            print(f'O cliente {self.nome} NÃO pode assistir o filme {filme}')
