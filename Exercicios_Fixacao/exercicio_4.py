"""
Exercício 4: Conteúdos até Aula 6.
"""


def cadastrar_livro(id):
    print('--------')
    print('---------- MENU CADASTRAR LIVRO ----------')
    print(f'Id do livro: {id}')
    nome = input('Por favor entre com o nome do livro: ')
    autor = input('Por favor entre com o autor do livro: ')
    editora = input('Por favor entre com a editora do livro: ')
    livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}
    lista_livros.append(livro.copy())


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
        if opcao_consulta == '4':
            return
        else:
            print('Opção inválida')


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
        id_global += 1
    elif opcao == '2':
        consultar_livro()
    elif opcao == '4':
        break
    else:
        print('Opção inválida')
