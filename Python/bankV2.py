from datetime import datetime

# Menus
startMenu = """\nBanco em terminal Python \n
Selecione uma ação que desejas usar:
[1] Depositar.
[2] Sacar.
[3] Histórico de transações.
[4] Sair do programa.\n
"""

depositMenu = "\nOpção de depositar escolhida.\nDigite o valor a depositar ou 'sair': "
withdrawMenu = "\nOpção de sacar escolhida.\nDigite o valor a sacar ou 'sair': "
newAccountMenu = "\nA conta não foi encontrada...\nCriando nova conta...\nDigite o número da nova conta: "
historyMenu = "\nHistórico de transações:"
loginMenu = "\nDigite o número da conta ou 'sair': "

# Accounts dictionary
accounts = {
    "1111": {"name": "Admin", "balance": 12000, "withdrawLimit": 3, "withdrawAttempts": 0, "history": []},
    "2222": {"name": "Test", "balance": 10, "withdrawLimit": 3, "withdrawAttempts": 0, "history": []},
    "3333": {"name": "Test2", "balance": 0, "withdrawLimit": 3, "withdrawAttempts": 0, "history": []}
}


def main():
    accountNum = login()

    while True:
        optionValue = input(startMenu).strip()

        match optionValue:
            case "1":
                deposit(accountNum)
            case "2":
                withdraw(accountNum)
            case "3":
                historyTransactions(accountNum)
            case "4":
                print("Saindo...")
                break
            case _:
                print("Opção inválida.")


def deposit(account):
    acc = accounts.get(account)
    if not acc:
        print("\nConta inválida.")
        return

    depositValue = input(depositMenu).strip()

    if depositValue.lower() == "sair":
        return

    if depositValue.isdigit() and int(depositValue) > 0:
        value = int(depositValue)
        acc["balance"] += value
        acc["history"].append(f"Depositou: R$ {value:.2f} às {datetime.now().strftime('%H:%M:%S')}")
        print(f"Depósito realizado. Saldo atual: R$ {acc['balance']:.2f}")
    else:
        print("Entrada inválida.")


def withdraw(account):
    acc = accounts.get(account)
    if not acc:
        print("\nConta inválida.")
        return

    withdrawValue = input(withdrawMenu).strip()

    if withdrawValue.lower() == "sair":
        return

    if withdrawValue.isdigit():
        value = int(withdrawValue)
        if value <= acc["balance"] and value > 0:
            acc["balance"] -= value
            acc["history"].append(f"Sacou: R$ -{value:.2f} às {datetime.now().strftime('%H:%M:%S')}")
            acc["withdrawAttempts"] += 1
            print(f"Saque realizado. Saldo atual: R$ {acc['balance']:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido.")
    else:
        print("Entrada inválida.")


def historyTransactions(account):
    acc = accounts.get(account)

    print(historyMenu)

    if not acc["history"]:
        print("\nNão há histórico de transações.")
    else:
        for i, entry in enumerate(acc["history"], start=1):
            print(f"{i}. {entry}")
    
    print(f"\nSaldo atual: R$ {acc['balance']:.2f}")


def login():
    loginAction = input(loginMenu).strip()

    if loginAction.lower() == "sair":
        exit()

    if loginAction not in accounts:
        print("Conta não encontrada.")
        createAccount(loginAction)

    return loginAction


def createAccount(newAccountNumber):
    if newAccountNumber in accounts:
        print("Essa conta já existe.")
        return

    name = input("Digite seu nome: ").strip()
    accounts[newAccountNumber] = {"name": name, "balance": 0,"withdrawLimit": 3, "withdrawAttempts": 0, "history": []}
    print("Conta criada com sucesso.")


main()
