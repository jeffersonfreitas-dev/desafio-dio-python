import datetime
from typing import Optional


def depositar(saldo: float, valor: float, extratos: list, /) -> tuple[float, list]:
    if valor and valor > 0:
        saldo += valor
        extratos.append(adicionar_movimento(valor, "DEPÓSITO"))
        print(f"Depósito R$ {valor:.2f} realizado com sucesso.")
    else:
        print(f"O valor {valor:.2f} não é válido")
    return saldo, extratos

def sacar(*, saldo:float, valor: float, extratos: list, limite: float, numero_saques: int, limite_saques: int) -> tuple[float, list]:
    if valor > saldo:
        print("Não possui saldo suficiente")
    elif valor > limite:
        print("Valor acima do limite")
    elif numero_saques >= limite_saques:
        print("Limite de saque excedido")
    else:
        saldo -= valor
        numero_saques += 1
        extratos.append(adicionar_movimento(valor, "SAQUE"))
        print(f"Saque de {valor:.2f} realizado com sucesso")
    return saldo, extratos

def adicionar_movimento(valor: float, movimento: str) -> str:
    return f"{datetime.date.today()}\t{movimento} NA CONTA\tVALOR {valor:.2f}"

def get_extrato(saldo: float, /, *, extratos: list) -> None:
    if len(extratos) == 0:
        print("Sem movimentações")
        return

    print("===== EXTRATO =======")
    for extrato in extratos:
        print(extrato)

    print(f"SALDO R$ : {saldo:.2f}")
    print("===== FIM DO EXTRATO =======")

def nova_conta(agencia: str, contas: list, usuarios: list) -> None:
    cpf = input("Informe o número do CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("Usuário inexistente")
        return

    numero_conta = len(contas) + 1
    conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    contas.append(conta)
    print(f"Conta {numero_conta} criada com sucesso!")

def listar_contas(contas: list) -> None:
    for conta in contas:
        linha = f"""
            Agência:\t{conta["agencia"]}
            Conta:\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
        print("=" * 50)
        print(linha)

def novo_usuario(usuarios: list) -> None:
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Usuário com este CPF já cadastrado")
        return

    nome = input("Informe o nome do novo usuário: ")
    data_nascimento = input("Informe a data de nascimento do novo usuário: ")
    endereco = input("Informe o endereço (logradouro, número, bairro, cidade/estado: ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print(f"Usuário com CPF {cpf} cadastrado com sucesso!")

def filtrar_usuario(cpf: str, usuarios: list) -> Optional[dict]:
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def main():
    menu = """
    (d) - Depositar
    (s) - Sacar
    (e) - Extrato
    (nc) - Nova Conta
    (lc) - Listar Contas
    (nu) - Novo Usuário
    (q) - Sair
    """

    saldo = 0.0
    limite = 500.0
    extratos = []
    numero_saques = 0
    usuarios = []
    contas = []
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    while True:
        opcao = input(menu)

        match opcao:
            case "d":
                valor = float(input("Informe o valor para depósito: "))
                saldo, extratos = depositar(saldo, valor, extratos)
            case "s":
                valor_saque = float(input("Informe o valor para saque: "))
                saldo, extratos = sacar(
                    saldo=saldo,
                    valor=valor_saque,
                    extratos=extratos,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES)
            case "e":
                get_extrato(saldo, extratos=extratos)
            case "nc":
                nova_conta(AGENCIA, contas, usuarios)
            case "lc":
                listar_contas(contas)
            case "nu":
                novo_usuario(usuarios)
            case "q":
                break
            case _:
                print("Opção inválida!")


main()