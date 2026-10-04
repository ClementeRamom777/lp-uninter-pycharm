"""

Exercício 1: Conteúdos até Aula 3.

"""

print('Boas-vindas Ramom Siqueira') # Print de mensagem de boas-vindas.
valor_unitario = float(input('Insira o valor unitário: ')) # Linha 8 e 9 recebem inputs do valor unitário e quantidade de produtos pelo usuário.
quantidade = int(input('Insira a quantidade: '))
valor_total = quantidade * valor_unitario # A variável valor_total recebe a multiplicação da quantidade com o valor unitário.
if valor_total < 2500: # Se valor_total for menor que 2500 o desconto será 0%
    valor_com_desconto = valor_total * 1.0
elif valor_total < 6000: # Se valor_total for maior ou igual que 2500 e menor que 6000 o desconto será de 4%
    valor_com_desconto = valor_total * 0.96
elif valor_total < 10000: # Se valor_total for maior ou igual que 6000 e menor que 10000 o desconto será de 7%
    valor_com_desconto = valor_total * 0.93
else: # Se valor_total for maior ou igual que 10000 o desconto será de 11%
    valor_com_desconto = valor_total * 0.89
print(f'Valor SEM desconto. Total a pagar: R${valor_total:.2f}') # Linha 19 e 20 recebem os prints.
print(f'Valor COM desconto. Total a pagar: R${valor_com_desconto:.2f}')

