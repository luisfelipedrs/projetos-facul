# INÍCIO DO PROGRAMA, APRESENTAÇÃO DO NOME DA APLICAÇÃO E POSSÍVEIS OPERAÇÕES
print('-' * 22, '\nCALCULADORA EM PYTHON')
print('\nOPERAÇÕES:\n+\n-\n*\n/\nSAIR')

# LAÇO QUE MANTÊM O PROGRAMA FUNCIONANDO ATÉ QUE O USUÁRIO DIGITE A OPÇÃO "SAIR"
while True:
    operacao = input('\nSELECIONE UMA OPERAÇÃO: ')

    # ENCERRA O PROGRAMA CASO A OPÇÃO 'SAIR' SEJA DIGITADA, UTILIZANDO A FUNÇÃO UPPER PARA
    # QUE O INPUT FIQUE EM LETRAS MAIÚSCULAS
    if operacao.upper() == 'SAIR':
        print('NENHUMA OPERAÇÃO FOI SELECIONADA, O PROGRAMA SERÁ ENCERRADO.')
        break

    # INVALIDA A OPERACÃO CASO SEJA DIGITADA OUTRA OPÇÃO QUALQUER DIFERENTE DAS OPÇÕES
    # CITADAS
    elif operacao != '+' and operacao != '-' and operacao != '*' and operacao != '/':
        print('OPERAÇÃO INVÁLIDA')
        # SEGUE PARA A PRÓXIMA ITERAÇÃO
        continue

    # COLETA OS DADOS QUE SERÃO UTILIZADOS NA OPERAÇÃO, SENDO N1 O PRIMEIRO NÚMERO
    # E N2 O SEGUNDO
    n1 = float(input('SELECIONE O PRIMEIRO NÚMERO: '))
    n2 = float(input('SELECIONE O SEGUNDO NÚMERO: '))

    # CRIAÇÃO DE UMA VARIÁVEL PARA ARMAZENAR O VALOR DO RESULTADO, FACILITANDO ASSIM
    # A IMPRESSÃO DO MESMO NA TELA, SEM QUE SEJA PRECISO UTILIZAR O PRINT PARA TODOS
    # OS CASOS
    resultado = 0

    # REALIZA A OPERAÇÃO SOLICITADA
    if operacao == '+':
        resultado = n1 + n2

    elif operacao == '-':
        resultado = n1 - n2

    elif operacao == '*':
        resultado = n1 * n2

    elif operacao == '/':
        # INVALIDA A OPERAÇÃO CASO O NUMERADOR SELECIONADO SEJA = 0
        if n2 == 0:
            print('IMPOSSÍVEL DIVIDIR POR 0!')
            continue
        else:
            resultado = n1 / n2

    # IMPRIME NA TELA O RESULTADO FINAL DA OPERAÇÃO
    print(('{} ' + operacao + ' {} = {}.').format(n1, n2, resultado))
