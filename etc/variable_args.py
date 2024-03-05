# the idea here is that the function will support variable number of arguments, and than you decide what to do with them.
def f(galleons, sickles, knuts, *args, **kwargs):
    if not kwargs == {}:
        print("Positional:", kwargs)
    print((galleons * 17 + sickles) * 29 + knuts, "Knuts")

list = {"knuts": 25, "sickles": 50, "galleons": 100}

f(**list)