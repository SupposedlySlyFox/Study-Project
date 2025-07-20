from datetime import datetime

# Menu display text.
startMenu = """\nBanco em terminal Python \n
Selecione uma ação que desejas usar:
[1] Depositar.
[2] Sacar.
[3] Histórico de transações.
[4] Sair do programa.\n
"""

# Deposit menu display text.
depositMenu = """\nOpção de depositar escolhida.
Selecione o valor que gostaria depositar, ou digite 'sair' para voltar: """

# Withdraw menu display text.
withdrawMenu = """\nOpção de sacar escolhida.
Selecione o valor que gostaria sacar, ou digite 'sair' para voltar: """

# History of transaction menu display text.
historyMenu = "\nHistorico de transações:"

# User's balance.
balance = 0;

# Balance's history.
history = [];
        
# Main usage of the program.
def main():
    while True:
        optionValue = input(startMenu);

        match optionValue:
            case "1":
                deposit();

            case "2":
                withdraw();

            case "3":
                historyTransactions();

            case "4":
                break;

# Deposit certain value into balance.
def deposit():
    global balance, history

    depositValue = input(depositMenu);

    if depositValue.lower() == "sair":
        return 0;
    elif int(depositValue) > 0:
        balance += int(depositValue);
        history.append(f"\nDepositou: R$ +{int(depositValue):.2f} às {datetime.now().strftime('%H:%M:%S')}");
        print(f"\nSaque realizado. Saldo atual: R$ {balance:.2f}");
    else:
        print("\nEntrada Invalida ou Saldo insuficiente.");

# Withdraw certain value from the balance.
def withdraw():
    global balance, history

    withdrawValue = input(withdrawMenu);
    
    if withdrawValue.lower() == "sair":
        return 0;
    elif int(withdrawValue) <= balance and int(withdrawValue) > 0:
        balance -= int(withdrawValue);
        history.append(f"\nSacou: R$ -{int(withdrawValue):.2f} às {datetime.now().strftime('%H:%M:%S')}");
        print(f"\nSaque realizado. Saldo atual: R$ {balance:.2f}");
    else:
        print("\nEntrada Invalida ou Saldo insuficiente.");

# Display history of transaction and organized by time.
def historyTransactions():
    global balance, history

    print(historyMenu);

    if not history:
        print("\nNão há historico de transações.")
    else:
        for index in range(len(history)):
            print(f"{index + 1}. {history[index]}\n")

main();
