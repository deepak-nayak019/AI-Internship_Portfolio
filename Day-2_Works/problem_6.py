# BankAccount Class

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be greater than 0.")

    # Withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self.balance:
            print(f"Insufficient funds! Available balance: ₹{self.balance}")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    # Check balance
    def get_balance(self):
        print(f"{self.account_holder}'s Current Balance: ₹{self.balance}")


# ----------------------------
# Create Two Bank Accounts
# ----------------------------

account1 = BankAccount("Deepak", 5000)
account2 = BankAccount("Rahul", 2000)

# ----------------------------
# Transactions for Account 1
# ----------------------------

print("------ Account 1 ------")
account1.get_balance()

account1.deposit(1500)
account1.get_balance()

account1.withdraw(2000)
account1.get_balance()

account1.withdraw(6000)   # Insufficient funds
account1.get_balance()


# ----------------------------
# Transactions for Account 2
# ----------------------------

print("\n------ Account 2 ------")
account2.get_balance()

account2.deposit(1000)
account2.get_balance()

account2.withdraw(500)
account2.get_balance()

account2.withdraw(3000)   # Insufficient funds
account2.get_balance()