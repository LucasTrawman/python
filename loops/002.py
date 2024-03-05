str = input("Input: ")
noVogals = ""
for char in str:
    match char:
        case "A" | "E" | "I" | "O" | "U"| "a" | "e" | "i" | "o" | "u":
            noVogals += ""
        case _:
            noVogals += char
print(noVogals)
