def main():
    x = int(input("x: "))
    y = int(input("y: "))

    print(f"{x / y:,.2f}")
    print(f"x squared is {square(x)}")

def square(n):
    return pow(n, 2)

main()