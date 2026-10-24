"""
Exercício 5: Conteúdos até a aula prática 6.
"""

import random


def gerar_cartela(sigla):
    cartela = []
    for i in range(5):
        cartela.append([0, 0, 0, 0, 0])
    cartela[2][2] = sigla
    return cartela


print(gerar_cartela('RC'))