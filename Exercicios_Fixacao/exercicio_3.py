"""

Exercício 3: Conteúdos até Aula 5.

"""


# Mostra o menu de serviços e devolve o preço por página do escolhido.
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


# Pede o número de páginas e devolve a quantidade já com o desconto.
def num_pagina():
    while True:
        # Se digitarem letras, o int() falha e o except trata o erro.
        try:
            num_pagina = int(input('Entre com o número de páginas: '))
            # Faixas do enunciado: quanto mais páginas, maior o desconto.
            if num_pagina < 20:
                return num_pagina
            elif num_pagina < 200:
                return num_pagina * 0.85
            elif num_pagina < 2000:
                return num_pagina * 0.80
            elif num_pagina < 20000:
                return num_pagina * 0.75
            # Acima de 20000 páginas, recusa e pergunta de novo.
            else:
                print('Não aceitamos tantas páginas de uma vez.')
                print('Por favor, entre com o número de páginas novamente.')
        except ValueError:
            print('Valor inválido. Digite um número inteiro.')


# Pergunta pelo serviço extra e devolve o valor dele (0 se não houver).
def servico_extra():
    while True:
        print('Deseja adicionar algum serviço?')
        print('1 - Encadernação Simples - R$ 15.00')
        print('2 - Encadernação Capa Dura - R$ 40.00')
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
paginas = num_pagina()
extra = servico_extra()
# Total calculado fora das funções, pela fórmula do enunciado.
total = (servico * paginas) + extra
print(f'Total: R$ {total:.2f} (serviço: {servico:.2f} * páginas: {paginas:.0f} + extra: {extra:.2f})')
