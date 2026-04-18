class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(("deposit", amount))

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        self.transactions.append(("withdrawal", amount))

    def get_balance(self):
        return self.balance

class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount

class BankSystem:
    def __init__(self):
        self.users = []
        self.accounts = []

    def create_user(self, username, password):
        user = User(username, password)
        self.users.append(user)
        return user

    def create_account(self, account_number, balance=0):
        account = Account(account_number, balance)
        self.accounts.append(account)
        return account

    def assign_account_to_user(self, user, account):
        user.add_account(account)

    def get_user_accounts(self, user):
        return user.accounts

    def get_account_balance(self, account):
        return account.get_balance()

bank_system = BankSystem()
user1 = bank_system.create_user("user1", "password1")
account1 = bank_system.create_account("12345", 1000)
bank_system.assign_account_to_user(user1, account1)
account1.deposit(500)
account1.withdraw(200)
print(bank_system.get_account_balance(account1))
for transaction in account1.transactions:
    print(f"{transaction[0]} {transaction[1]}")

user2 = bank_system.create_user("user2", "password2")
account2 = bank_system.create_account("67890", 500)
bank_system.assign_account_to_user(user2, account2)
account2.deposit(200)
account2.withdraw(100)
print(bank_system.get_account_balance(account2))
for transaction in account2.transactions:
    print(f"{transaction[0]} {transaction[1]}")