class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Account:
    def __init__(self, user, balance=0):
        self.user = user
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
    def __init__(self, account, transaction_type, amount):
        self.account = account
        self.transaction_type = transaction_type
        self.amount = amount

class BankSystem:
    def __init__(self):
        self.accounts = []
        self.users = []

    def create_user(self, name, surname):
        self.users.append(User(name, surname))

    def create_account(self, user, balance=0):
        self.accounts.append(Account(user, balance))

    def get_user(self, name, surname):
        for user in self.users:
            if user.name == name and user.surname == surname:
                return user

    def get_account(self, user):
        for account in self.accounts:
            if account.user == user:
                return account

    def deposit(self, user, amount):
        account = self.get_account(user)
        account.deposit(amount)

    def withdraw(self, user, amount):
        account = self.get_account(user)
        account.withdraw(amount)

    def get_balance(self, user):
        account = self.get_account(user)
        return account.get_balance()

bank = BankSystem()
bank.create_user("John", "Doe")
user = bank.get_user("John", "Doe")
bank.create_account(user)
bank.deposit(user, 1000)
bank.withdraw(user, 500)
print(bank.get_balance(user))