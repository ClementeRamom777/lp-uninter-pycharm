"""

Exercício 2: Conteúdos até Aula 4.

"""

# Imprime a mensagem de boas-vindas.
print('Boas-vindas Ramom Siqueira Clemente')
total = 0
# Estrutura While, repete o pedido até o cliente responder N.
while True:
    # Input do sabor
    sabor = input('Entre com o sabor desejado (CP/AC): ')
    if sabor == 'CP' or sabor == 'AC' or sabor == 'ac' or sabor == 'cp':
        # Input tamanho
        tamanho = input('Entre com o tamanho desejado (P/M/G): ')
        if (tamanho == 'P' or tamanho == 'M' or tamanho == 'G'
                or tamanho == 'p' or tamanho == 'm' or tamanho == 'g'):
            # Preço de cada combinação de sabor e tamanho.
            if sabor == 'CP' or sabor == 'cp':
                if tamanho == 'P' or tamanho == 'p':
                    valor = 9
                    print(f'Você pediu um Cupuaçu no tamanho P: R$ {valor:.2f}')
                elif tamanho == 'M' or tamanho == 'm':
                    valor = 14
                    print(f'Você pediu um Cupuaçu no tamanho M: R$ {valor:.2f}')
                else:
                    valor = 18
                    print(f'Você pediu um Cupuaçu no tamanho G: R$ {valor:.2f}')
            else:
                if tamanho == 'P' or tamanho == 'p':
                    valor = 11
                    print(f'Você pediu um Açai no tamanho P: R$ {valor:.2f}')
                elif tamanho == 'M' or tamanho == 'm':
                    valor = 16
                    print(f'Você pediu um Açai no tamanho M: R$ {valor:.2f}')
                else:
                    valor = 20
                    print(f'Você pediu um Açai no tamanho G: R$ {valor:.2f}')
            # Acumulador que soma os valores dos pedidos.
            total = total + valor
            # Pergunta se o cliente quer mais; N encerra o laço.
            resposta = input('Deseja mais alguma coisa? (S/N): ')
            if resposta == 'N' or resposta == 'n':
                break
        else:
            # Tamanho fora de P, M ou G.
            print('Tamanho inválido. Tente novamente')

            # Volta ao início para pedir o sabor de novo.
            continue
    else:
        # Sabor fora de CP ou AC.
        print('Sabor inválido. Tente novamente')
        # Estrutura continue, volta ao início para pedir o sabor de novo.
        continue
print(f'O valor total a ser pago: R$ {total:.2f}')
