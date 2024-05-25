class BankAccount():
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")
    
    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
    
    def print(self):
        print(f"Current balance: {self.balance}")
        print(f"Interest rate: {self.interest_rate}")


bank_account = BankAccount("147258369", "sizar shaaban")
bank_account.deposit(1000)
print(f"Current balance: {bank_account.get_balance()}")
bank_account.withdraw(500)
print(f"Current balance: {bank_account.get_balance()}")


savings_account = SavingsAccount("741852963", "sizar shaaban", 0.05)
savings_account.deposit(1000)
savings_account.apply_interest()
savings_account.print()
