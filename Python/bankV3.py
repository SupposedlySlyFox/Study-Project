from datetime import datetime

class Account:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.balance = 0
        self.withdraw_limit = 3
        self.withdraw_attempts = 0
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Valor inválido para depósito.")
            return
        self.balance += amount
        self._add_history(f"Depositou: R$ {amount:.2f}")
        print(f"Depósito realizado. Saldo atual: R$ {self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Valor inválido para saque.")
            return
        if amount > self.balance:
            print("Saldo insuficiente.")
            return
        self.balance -= amount
        self.withdraw_attempts += 1
        self._add_history(f"Sacou: R$ -{amount:.2f}")
        print(f"Saque realizado. Saldo atual: R$ {self.balance:.2f}")

    def show_history(self):
        print("\nHistórico de transações:")
        if not self.history:
            print("Não há histórico de transações.")
        else:
            for i, entry in enumerate(self.history, start=1):
                print(f"{i}. {entry}")
        print(f"\nSaldo atual: R$ {self.balance:.2f}")

    def _add_history(self, entry):
        timestamp = datetime.now().strftime('%H:%M:%S')
        self.history.append(f"{entry} às {timestamp}")


class Bank:
    def __init__(self):
        self.accounts = {}
        self._load_initial_accounts()

    def _load_initial_accounts(self):
        self.accounts["1111"] = Account("1111", "Admin")
        self.accounts["1111"].balance = 12000
        self.accounts["2222"] = Account("2222", "Test")
        self.accounts["2222"].balance = 10
        self.accounts["3333"] = Account("3333", "Test2")

    def run(self):
        account = self._login()

        while True:
            option = input(self._start_menu()).strip()
            match option:
                case "1":
                    self._handle_deposit(account)
                case "2":
                    self._handle_withdraw(account)
                case "3":
                    account.show_history()
                case "4":
                    print("Saindo...")
                    break
                case _:
                    print("Opção inválida.")

    def _start_menu(self):
        return """\nBanco em terminal Python

Selecione uma ação que desejas usar:
[1] Depositar.
[2] Sacar.
[3] Histórico de transações.
[4] Sair do programa.\n"""

    def _login(self):
        while True:
            account_number = input("\nDigite o número da conta ou 'sair': ").strip()
            if account_number.lower() == "sair":
                exit()

            account = self.accounts.get(account_number)
            if account:
                return account

            print("\nConta não encontrada...")
            self._create_account(account_number)

    def _create_account(self, number):
        name = input("Digite seu nome: ").strip()
        if number in self.accounts:
            print("Conta já existente.")
        else:
            self.accounts[number] = Account(number, name)
            print("Conta criada com sucesso.")

    def _handle_deposit(self, account):
        while True:
            user_input = input("\nOpção de depositar escolhida.\nDigite o valor a depositar ou 'sair': ").strip()
            if user_input.lower() == "sair":
                return
            if user_input.isdigit():
                account.deposit(int(user_input))
                return
            print("Entrada inválida.")

    def _handle_withdraw(self, account):
        while True:
            user_input = input("\nOpção de sacar escolhida.\nDigite o valor a sacar ou 'sair': ").strip()
            if user_input.lower() == "sair":
                return
            if user_input.isdigit():
                account.withdraw(int(user_input))
                return
            print("Entrada inválida.")


if __name__ == "__main__":
    bank = Bank()
    bank.run()
