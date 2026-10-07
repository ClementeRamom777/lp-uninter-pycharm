"""
Exercício 2: Conteúdos até Aula 4.
"""

print('Boas-vindas Ramom Clemente')
while True:
    sabor = input('Entre com o sabor desejado (CP/AC): ')
    if sabor == 'CP' or sabor == 'AC' or sabor == 'ac' or sabor == 'cp':
        print("Sabor válido")
    else:
        print('Sabor inválido. Tente novamente')
        continue