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
        print(' Depósito '.center(35, '-'))
        if deposito > 0:
            saldo += deposito
            extrato += f'Depósito: R$ {deposito:.2f}\n'
            print(f'R$ {deposito:.2f}')
        else:
            print('Valor não pode ser negativo.')
        print('-'.center(35, '-'))

    elif opcao == 's':
        saque = float(input('Informe o valor do saque: '))
        print(' Saque '.center(35, '-'))

        saldo_insuficiente = saque > saldo

        excedeu_limite = saque > LIMITE

        excedeu_limite_saques = numero_saques >= LIMITE_SAQUES

        if saldo_insuficiente:
            print('Saldo insuficiente!')

        elif excedeu_limite:
            print(f'Excedeu o limite de R$ {LIMITE:.2F} para saque.')

        elif excedeu_limite_saques:
            print(f'Excedeu o limite de {LIMITE_SAQUES} saques.')

        elif saque > 0:
            saldo -= saque
            extrato += f'Saque: R$ {saque:.2f}\n'
            numero_saques += 1
            print(f'- R$ {saque:.2f}')

        print('-'.center(35, '-'))

    elif opcao == 'e':
        print(' Extrato '.center(35, '-'))
        if not extrato:
            print('Não houveram movimentações.')
        print(extrato)
        print(f'Valor em conta: R$ {saldo:.2f}')
        print('-'.center(35, '-'))

    elif opcao == 'q':
        print('-'.center(35, '-'))
        print('Saindo...')
        print('-'.center(35, '-'))
        break

    else:
        print('-'.center(35, '-'))
        print('Opção inválida! Tente novamente.')
        print('-'.center(35, '-'))
