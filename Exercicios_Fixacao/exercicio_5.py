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


print(gerar_cartela('RC'))
