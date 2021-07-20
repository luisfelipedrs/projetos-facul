from random import randint

cont_vitorias = resultado = total = 0

while True:
    comp = randint(0, 10)
    opcao_player = str(input('Par ou ímpar? [P/I]: ')).strip().upper()[0]

    if opcao_player not in 'PpIi':
        print('Opção inválida!')
        break

    player = int(input('Digite um número: '))

    if (comp + player) % 2 == 0:
        resultado = 'Par'
        total = player + comp

        if opcao_player in 'Pp':
            cont_vitorias += 1
            print(f'Você ganhou {cont_vitorias} vezes seguidas, jogou {player} e o computador jogou {comp}, o resultado total de {total} deu {resultado}!')

        elif opcao_player not in 'Pp':
            print(f'Você perdeu, o computador jogou {comp} e você jogou {player}, e o resultado total de {total} deu {resultado}!')
            print('Tente novamente!')
            break

    elif (comp + player) % 2 != 0:
        resultado = 'Impar'
        total = player + comp

        if opcao_player in 'Ii':
            cont_vitorias += 1
            print(f'Você ganhou {cont_vitorias} vezes seguidas, jogou {player} e o computador jogou {comp}, o resultado total de {total} deu {resultado}!')

        elif opcao_player not in 'Ii':
            print(f'Você perdeu, o computador jogou {comp} e você jogou {player}, e o resultado total de {total} deu {resultado}!')
            print('Tente novamente!')
            break

print(f'Você ganhou {cont_vitorias} vezes seguidas!')
