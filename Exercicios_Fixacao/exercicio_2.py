"""

Exercício 2: Conteúdos até Aula 4.

"""

print('Boas-vindas Ramom Siqueira Clemente')
while True:
    sabor = input('Entre com o sabor desejado (CP/AC): ')
    if sabor == 'CP' or sabor == 'AC' or sabor == 'ac' or sabor == 'cp':
       tamanho = input('Entre com o tamanho desejado (P/M/G): ')
       if tamanho == 'P' or tamanho == 'M' or tamanho == 'G' or tamanho == 'p' or tamanho == 'm' or tamanho == 'g':
           if sabor == 'CP' or sabor == 'cp':
                if tamanho == 'P' or tamanho == 'p':
                    valor = 9
       else:
           print('Tamanho inválido. Tente novamente')
           continue
    else:
        print('Sabor inválido. Tente novamente')
        continue
