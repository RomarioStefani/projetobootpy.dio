menu =  """

[d] Deposito
[s] Saque
[e] Extrato
[s] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        valor = float(input("Informe o valor do depósito."))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou, o valor informado é inválido")    

    elif opcao == "s":
        print("saque")

        valor = float(input("Quanto deseja sacar?"))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente.")

        elif excedeu_limite:
            print("Limite insuficiente.")

        elif excedeu_saques:
            print("Limite de saques diarios atingido.")

        elif valor > 0 :
            saldo -= valor
            extrato += f"Saque R$ {valor:.2f}\n"
            numero_saques += 1 

        else:
            print("Falha na operação, o valor informado é invalido.")


    elif opcao == "e":
        print("\n===============EXTRATO=============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo = R$: {saldo:.2f}")
        print("======================================")


    elif opcao == "s":
        break

    else:
        ("Operação invalida, selecione novamente a opção desejada.")