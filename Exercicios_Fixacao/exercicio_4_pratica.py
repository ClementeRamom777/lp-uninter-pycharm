"""
Exercício 4: Conteúdos até Aula 6.
"""


# Cadastra um livro com o id recebido do menu principal (id_global).
def cadastrar_livro(id):
    print('--------')
    print('---------- MENU CADASTRAR LIVRO ----------')
    print(f'Id do livro: {id}')
    nome = input('Por favor entre com o nome do livro: ')
    autor = input('Por favor entre com o autor do livro: ')
    editora = input('Por favor entre com a editora do livro: ')
    livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}
    # .copy() guarda uma cópia, não um segundo nome para o dicionário.
    lista_livros.append(livro.copy())


# Submenu de consulta; repete até o usuário escolher 4 (return).
def consultar_livro():
    while True:
        print('--------------------------------------------------')
        print('---------- MENU CONSULTAR LIVRO -------------------')
        print('Escolha a opção desejada:')
        print('1 - Consultar Todos os Livros')
        print('2 - Consultar Livro por id')
        print('3 - Consultar Livro(s) por autor')
        print('4 - Retornar')
        opcao_consulta = input('>>')
        if opcao_consulta == '1':
            print('----------------')
            for livro in lista_livros:
                for chave, valor in livro.items():
                    print(f'{chave}: {valor}')
                print()
            print('----------------')
        elif opcao_consulta == '2':
            # int(): o input devolve texto e o id foi guardado como número.
            id_busca = int(input('Digite o id do livro: '))
            print('----------------')
            for livro in lista_livros:
                if livro['id'] == id_busca:
                    for chave, valor in livro.items():
                        print(f'{chave}: {valor}')
                    print()
            print('----------------')
        elif opcao_consulta == '3':
            autor_busca = input('Digite o autor do(s) livro(s): ')
            print('----------------')
            for livro in lista_livros:
                if livro['autor'] == autor_busca:
                    for chave, valor in livro.items():
                        print(f'{chave}: {valor}')
                    print()
            print('----------------')
        elif opcao_consulta == '4':
            return
        else:
            print('Opção inválida')


def remover_livro():
    print('--------------------------------------------------')
    print('------------- MENU REMOVER LIVRO -----------------')
    while True:
        id_remover = int(input('Digite o id do livro a ser removido: '))
        for livro in lista_livros:
            if livro['id'] == id_remover:
                lista_livros.remove(livro)
                print('Livro removido com sucesso!')
                return
        # Só chega aqui se o for terminou sem achar o id (sem return).
        print('Id inválido')


print('Boas-vindas Ramom Siqueira Clemente')
lista_livros = []
id_global = 5598100
while True:
    print('--------------------------------------------------')
    print('--------------- MENU PRINCIPAL -------------------')
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livro(s)')
    print('3 - Remover Livro')
    print('4 - Sair')
    opcao = input('>>')
    if opcao == '1':
        cadastrar_livro(id_global)
        # Avança o id para o próximo livro não repetir o número.
        id_global += 1
    elif opcao == '2':
        consultar_livro()
    elif opcao == '3':
        remover_livro()
    elif opcao == '4':
        break
    else:
        print('Opção inválida')
