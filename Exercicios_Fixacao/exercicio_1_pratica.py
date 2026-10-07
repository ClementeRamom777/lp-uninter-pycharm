"""

Exercício 1: Conteúdos até Aula 3.

"""

print('Boas-vindas Ramom Clemente')
valor_unitario = float(input('Insira o valor unitário: '))
quantidade = int(input('Insira a quantidade: '))
valor_total = quantidade * valor_unitario
if valor_total < 2500:
    valor_com_desconto = valor_total * 1.0
    print(f'Sem desconto. Total a pagar: R${valor_com_desconto:.2f}')
elif valor_total < 6000:
    valor_com_desconto = valor_total * 0.96
    print(f'Valor SEM desconto. Total a pagar: R${valor_total:.2f}')
    print(f'Valor COM desconto. Total a pagar: R${valor_com_desconto:.2f}')
elif valor_total < 10000:
    valor_com_desconto = valor_total * 0.93
    print(f'Valor SEM desconto. Total a pagar: R${valor_total:.2f}')
    print(f'Valor COM desconto. Total a pagar: R${valor_com_desconto:.2f}')
else:
    valor_com_desconto = valor_total * 0.89
    print(f'Valor SEM desconto. Total a pagar: R${valor_total:.2f}')
    print(f'Valor COM desconto. Total a pagar: R${valor_com_desconto:.2f}')

