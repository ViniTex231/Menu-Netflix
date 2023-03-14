cadastro = []
clientes = []
novo_usuario = []
filmes = []

def menu():
    while True:
        print('[0] - Sair\n'
              '[1] - Cadastrar\n'
              '[2] - Entrar\n'
              '[3] - Registrar filme\n'
              '[4] - Listar filmes\n')
        op = int(input('Escolha a opção: '))
        if op == 0:
            break


        elif op ==1:
            nome = input('Nome: ')
            cadastro.append(nome)
            email = input('Email: ')
            cadastro.append(email)
            print('Planos: | basic | medium | premium |')
            planos = ['basic', 'medium', 'premium']
            while True:
                plano = input('Plano: ').lower().strip()
                if plano in planos:
                    break
                else:
                    print('Plano inválido')
                cadastro.append(plano)
                clientes.append(cadastro[:])
                cadastro.clear()
                print(clientes)

        elif op == 2:
            while True:
                cliente = input('Nome: ')
                for i in range(len(clientes)):
                    if cliente == clientes[i][0]:
                        novo_usuario.append(clientes[i][0])
                        novo_usuario.append(clientes[i][1])
                        novo_usuario.append(clientes[i][2])
                        break
                print('Cliente não cadastrado')

        elif op == 3:
            nome_filme = input('Digite o nome do filme: ')
            filmes.append(nome_filme)
            categoria_filme = input('Qual o plano do filme? | Basic | Medium | Premium | ')
            filmes.append(categoria_filme)
            print(f'Foi adicionado o filme {nome_filme} para o plano {categoria_filme}.')

        elif op == 4:
            print(filmes)
menu()

