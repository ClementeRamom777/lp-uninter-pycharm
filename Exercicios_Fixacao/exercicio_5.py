"""
Exercício 5: Conteúdos até a aula prática 6.
"""

import random


def gerar_cartela(sigla):
    cartela = []
    for i in range(5):
        cartela.append([0, 0, 0, 0, 0])
    for coluna in range(5):
        inicio = coluna * 15 + 1
        fim = inicio + 14
        usados = []
        for linha in range(5):
            while True:
                numero = random.randint(inicio, fim)
                if numero not in usados:
                    usados.append(numero)
                    cartela[linha][coluna] = numero
                    break
    cartela[2][2] = sigla
    return cartela


def imprimir_cartela(cartela):
    for i in range(5):
        for j in range(5):
            if i == 2 and j == 2:
                print(f'[{cartela[i][j]}]', end=' ')
            elif cartela[i][j] < 10:
                print(f'[0{cartela[i][j]}]', end=' ')
            else:
                print(f'[{cartela[i][j]}]', end=' ')
        print()


def sorteia_valor(sorteados):
    if len(sorteados) >= 75:
        return -1
    while True:
        numero = random.randint(1, 75)
        if numero not in sorteados:
            return numero


def verifica_ganhador_cheia(cartelas, sorteados):
    for cartela in cartelas:
        completa = True
        for i in range(5):
            for j in range(5):
                if i == 2 and j == 2:
                    continue
                if cartela[i][j] not in sorteados:
                    completa = False
        if completa:
            return cartela
    return None


def verifica_ganhador_LCD(cartelas, sorteados):
    for cartela in cartelas:
        for i in range(5):
            completa = True
            for j in range(5):
                if i == 2 and j == 2:
                    continue
                if cartela[i][j] not in sorteados:
                    completa = False
            if completa:
                return cartela
        for j in range(5):
            completa = True
            for i in range(5):
                if i == 2 and j == 2:
                    continue
                if cartela[i][j] not in sorteados:
                    completa = False
            if completa:
                return cartela
        completa = True
        for i in range(5):
            if i != 2 and cartela[i][i] not in sorteados:
                completa = False
        if completa:
            return cartela
        completa = True
        for i in range(5):
            if i != 2 and cartela[i][4 - i] not in sorteados:
                completa = False
        if completa:
            return cartela
    return None


cartelas = []
regra = '1'
while True:
    print('Escolha a opção: ')
    print('1 - Gerar Cartelas')
    print('2 - Definir Regras')
    print('3 - Começar Bingo!')
    print('4 - Encerrar Programa')
    opcao = input('>>')
    if opcao == '1':
        cartelas = []
        quantidade = int(input('Informe a quantidade de cartelas a serem Geradas: '))
        for i in range (quantidade):
            cartelas.append(gerar_cartela('RC'))
    elif opcao == '2':
        print('Escolha a regra: ')
        print('1 - Linha, Coluna, Diagonal (padrão)')
        print('2 - Cartela Cheia')
        regra = input('>> ')
        if regra != '2':
            regra = '1'
    elif opcao == '3':
        print('Começando o Bingo!')
        sorteados = []
        while True:
            valor = sorteia_valor(sorteados)
            if valor == -1:
                break
            sorteados.append(valor)
            if regra == '2':
                ganhadora = verifica_ganhador_cheia(cartelas, sorteados)
            else:
                ganhadora = verifica_ganhador_LCD(cartelas, sorteados)
            if ganhadora is not None:
                print('Temos um ganhador!!')
                print(f'Sorteados: {len(sorteados)} números')
                imprimir_cartela(ganhadora)
                break
    elif opcao == '4':
        break
    else:
        print('Opção inválida')