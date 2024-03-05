def main():
    list = ["This", "is", "CS50"]
    yell1(*list)
    yell2("This", "is", "CS50")

def yell1(*words): #using map function to transform every argument in to an uppercase version
    uppercased = map(str.upper, words)
    print(*uppercased)

def yell2(*words): #same thing as yell1 but using list comprehensions "pythonic way"
    uppercased = [word.upper() for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()