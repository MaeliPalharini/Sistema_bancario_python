menu = """

[d] Depositar
[s] Sacar
[t] Transferencia
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
numero_transferencia = 0
LIMITE_TRANSFERENCIA = 5

while True:

    opcao = input(menu)

    if opcao.lower() == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Obaaaa, caiu graninhaa *__*!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao.lower() == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")
    if opcao.lower() == "t":
        transferencia = float(input("Informe o valor da transferência: "))
        banco_destino = input("Informe a letra inicial do seu banco:").upper()

        transferencia_excedeu_saldo = transferencia > saldo

        excedeu_transferencia = numero_transferencia >= LIMITE_TRANSFERENCIA

        banco_valido = banco_destino in ["N", "I", "B", "S"]

        if not banco_valido:
            print("Operação falhou! Banco destino não permitido.")

        elif transferencia_excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_transferencia:
            print("Operação falhou! Número máximo de transferência excedido.")

        elif transferencia > 0:
            saldo -= transferencia
            extrato += f"Transferência para banco {banco_destino}: R$ {transferencia:.2f}\n"
            numero_transferencia += 1
            print("Transferência realizada com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao.lower() == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(f"\n")
        print("==========================================")

    elif opcao.lower() == "q":
        break

    else:
        print("Por favor selecione novamente a operação desejada.")
