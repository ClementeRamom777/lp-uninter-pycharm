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


def num_pagina():
  while True:
    try:
        num_pagina = int(input('Entre com o número de páginas: '))
        if num_pagina < 20:
            return num_pagina
        elif num_pagina < 200:
            return num_pagina * 0.85
        elif num_pagina < 2000:
            return num_pagina * 0.80
        elif num_pagina < 20000:
            return num_pagina * 0.75
        else:
            print('Não aceitamos tantas páginas de uma vez.')
            print('Por favor, entre com o número de páginas novamente.')
    except ValueError:
        print('Valor inválido. Digite um número inteiro.')


def servico_extra():
    while True:
        print('Deseja adicionar algum serviço?')
        print('1 - Encardernação Simples - R$ 15.00')
        print('2 - Encardernação Capa Dura - R$ 40.00')
        print('0 - Não desejo mais nada')
        extra = input('>>')
        if extra == '1':
            return 15
        elif extra == '2':
            return 40
        elif extra == '0':
            return 0
        else:
            print('Opção inválida, entre com o serviço adicional novamente.')


print('Boas-vindas Ramom Siqueira Clemente')
servico = escolha_servico()
print(servico)
paginas = num_pagina()
print(paginas)
extra = servico_extra()
print(extra)