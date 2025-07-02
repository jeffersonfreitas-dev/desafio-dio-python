import datetime

menu = """
(d) - Depositar
(s) - Sacar
(e) - Extrato
(q) - Sair
"""

saldo = 0.0
limite = 500.0
extratos = []
numero_saques = 0
LIMITE_SAQUES = 3


def depositar(deposito: float) -> None:
    global saldo
    if deposito and deposito > 0:
        saldo += deposito
        adicionar_movimento(valor, "DEPÓSITO")
        print(f"Depósito R$ {deposito:.2f} realizado com sucesso.")
    else:
        print(f"O valor {deposito:.2f} não é válido")

def sacar(valor: float) -> None:
    global saldo, numero_saques
    if valor > saldo:
        print("Não possui saldo suficiente")
    elif valor > limite:
        print("Valor acima do limite")
    elif numero_saques >= LIMITE_SAQUES:
        print("Limite de saque excedido")
    else:
        saldo -= valor
        numero_saques += 1
        adicionar_movimento(valor, "SAQUE")

def adicionar_movimento(valor: float, movimento: str) -> None:
    extratos.append(f"{datetime.date.today()}\t{movimento} NA CONTA\tVALOR {valor:.2f}")


def get_extrato() -> None:
    if len(extratos) == 0:
        print("Sem movimentações")
        return

    print("===== EXTRATO =======")
    for extrato in extratos:
        print(extrato)

    print(f"SALDO R$ : {saldo:.2f}")



while True:
    opcao = input(menu)

    match opcao:
        case "d":
            valor = float(input("Informe o valor para depósito: "))
            depositar(valor)
        case "s":
            valor_saque = float(input("Informe o valor para saque: "))
            sacar(valor_saque)
        case "e":
            get_extrato()
        case "q":
            break
        case _:
            print("Opção inválida!")