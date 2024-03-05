x = input("camelCase: ")
z = x[0].lower()
for i in x[1:]: # You can use [1:] to tell from which position you'll start the loop, and you can use to determine the ending too
    if i.isupper():
        z += "_" + i.lower()
    else:
        z += i

print(f"snake_case: {z}")