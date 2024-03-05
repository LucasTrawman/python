def main():
    x = input("Greeting: ")
    print(f"${value(x)}")

def value(x):
    x = x.strip().lower()
    if x.startswith("hello"):
        return 0
    elif x[0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()