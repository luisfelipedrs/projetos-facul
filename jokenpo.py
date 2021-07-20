import random
from time import sleep

print('=' * 10, 'JOKENPO', '=' * 10)
print('''SUAS OPÇÕES:
[1] PEDRA
[2] PAPEL
[3] TESOURA
[4] SAIR''')

jogador = 0

while True:

    opcao = input('\nQual será sua jogada? ')


    if opcao == '1':
        jogador = 'Pedra'

    elif opcao == '2':
        jogador = 'Papel'

    elif opcao == '3':
        jogador = 'Tesoura'

    elif opcao == '4':
        print('O jogo será encerrado.')
        break

    else:
        print('OPÇÃO INVÁLIDA!')
        break

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')

    computador = random.randint(1, 3)

    if computador == 1:
        computador = 'Pedra'

    elif computador == 2:
        computador = 'Papel'

    elif computador == 3:
        computador = 'Tesoura'

    print('\nVocê jogou {} e o computador jogou {}!'.format(jogador, computador))

    resultado = 0

    if jogador == computador:
        resultado = 'Empate'

    elif jogador == 'Pedra' and computador == 'Papel':
        resultado = 'Computador venceu!'

    elif jogador == 'Papel' and computador == 'Tesoura':
        resultado = 'Computador venceu!'

    elif jogador == 'Tesoura' and computador == 'Pedra':
        resultado = 'Computador venceu!'


    elif computador == 'Pedra' and jogador == 'Papel':
        resultado = 'Jogador venceu!'

    elif computador == 'Papel' and jogador == 'Tesoura':
        resultado = 'Jogador venceu!'

    elif computador == 'Tesoura' and jogador == 'Pedra':
        resultado = 'Jogador venceu!'

    print('\n' + resultado)
