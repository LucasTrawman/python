# how to use global variables
# try to not use it
balance = 0

def main():
    print("Balance: ", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()

#don't use a local variable with the same name as a global variable that you pretend to use inside this same function