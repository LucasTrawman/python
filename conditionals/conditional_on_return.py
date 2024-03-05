def main():
    x = int(input("What's x? "))
    if is_even2(x):
        print("Even")
    else:
        print("Odd")

#normal way
def is_even1(n):
    if n % 2 == 0:
        return True
    else:
        return False

#pythonic way
def is_even2(n):
    return True if n % 2 == 0 else False

#better way
def is_even3(n):
    return n % 2 == 0



main()