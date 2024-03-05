class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print(f"Balance: {account.balance}")
    account.deposit(100)
    account.withdraw(20)
    print(f"Balance: {account.balance}")

if "__main__" == __name__:
    main()