def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "sheep" * i # the yield will send one group of sheeps at a time, making the program not crash for big datas

if __name__ == "__main__":
    main()