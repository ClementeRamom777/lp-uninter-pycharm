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


print('Boas-vindas Ramom Siqueira Clemente')
lista_livros = []
id_global = 5598100