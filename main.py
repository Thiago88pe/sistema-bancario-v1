MENU = '''
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair
Selecione a opção desejada: '''
saldo = 0
LIMITE = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(MENU)

    if opcao == 'd':
        deposito = float(input('Informe o valor para depósito: '))

    elif opcao == 's':
        saque = float(input('Informe o valor do saque: '))

    elif opcao == 'e':
        print(' Extrato '.center(35, '-'))

    elif opcao == 'q':
        print('-'.center(35, '-'))
        print('Saindo...')
        print('-'.center(35, '-'))
        break

    else:
        print('-'.center(35, '-'))
        print('Opção inválida! Tente novamente.')
        print('-'.center(35, '-'))
