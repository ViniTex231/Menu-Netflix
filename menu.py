from netflix import Cliente
from create import inserir_fimes
from create import inserir_usuario

usuario = []
usuarios = []
escolhido = ['###', '', '', '###']
planos = ['basic', 'medium', 'premium']



def menu():
    while True:
        print('---------------------\n'
              '[0] - Sair\n'
              '[1] - Cadastrar Usuário\n'
              '[2] - Cadastrar Filme\n'
              '[3] - Login\n'
              '[4] - Listar Filmes\n'
              '---------------------\n')
        op = int(input('Escolha a opção: '))
        if op == 0:
            break

        elif op == 1:
            inserir_usuario()

        elif op == 2:
            inserir_fimes()

        elif op == 3:
            pass
