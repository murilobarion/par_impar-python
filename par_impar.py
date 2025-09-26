import random
jogador = 0
computador = 0

while True:
    print('--------------JOGO DO PAR OU IMPAR-----------------')
    escolha = input('Escolhe aí 1 para par e 2 para ímpar: ')
    
    if escolha != '1' and escolha != '2':
        print('Escolha inválida! Digite 1 para par ou 2 para ímpar.')

    else:
        numero = int(input('digita seus numero (0-5): '))
        aleatorio = random.randint(0, 5)

        print(f'\nComputador: {aleatorio}')
        soma = numero + aleatorio
        print(f'Soma: {soma}\n')

        if (soma % 2 == 0 and escolha == '1') or (soma % 2 != 0 and escolha == '2'):
            print('ganhou!!!!')
            jogador  += 1
        else:
            print('perdeu!!!!')
            computador += 1
        print(f'Computador: {computador}')
        print(f'Jogador: {jogador}\n')

    if jogador == 5 or computador == 5:
        print('----------PERDEU----------\n')
        novo_jogo = int(input('Digite 1 para continuar e 2 para não continuar: '))
        if novo_jogo != 1 :
            break
