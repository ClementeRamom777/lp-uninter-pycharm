"""
Exercício 5: Conteúdos até a aula prática 6.
"""

import random


def gerar_cartela(sigla):
    cartela = []
    for i in range(5):
        cartela.append([0, 0, 0, 0, 0])
    usados = []
    for linha in range(5):
        while True:
            numero = random.randint(1, 15)
            if numero not in usados:
                usados.append(numero)
                cartela[linha][0] = numero
                break
    cartela[2][2] = sigla
    return cartela


print(gerar_cartela('RC'))