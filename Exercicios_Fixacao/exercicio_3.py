"""

Exercício 3: Conteúdos até Aula 5.

"""


def escolha_servico():
    while True:
        print('Entre com o tipo de serviço desejado: ')
        print('DIG - Digitalização')
        print('ICO - Impressão Colorida')
        print('IPB - Impressão Preto e Branco')
        print('FOT - Fotocópia')
        servico = input('>>')
        if servico == 'DIG' or servico == 'dig':
            return 1.10
        elif servico == 'ICO' or servico == 'ico':
            return 1.00
        elif servico == 'IPB' or servico == 'ipb':
            return 0.40
        elif servico == 'FOT' or servico == 'fot':
            return 0.20
        else:
            print('Escolha inválida, entre com o tipo do serviço novamente.')
print('Boas-vindas Ramom Siqueira Clemente')
servico = escolha_servico()
print(servico)
