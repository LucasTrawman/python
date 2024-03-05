def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x: "))
        except ValueError: # You will have to say what type of error will make you enter this block of code
            print("X is not integer")
            # pass - this would just enter the except block and do nothing, repeating the loop

main()