#for you to put arguments when calling a program
# ex: cat.py -n 3
# You will pass -n 3 so that argparse will capt and make the progam print meow 3 times

import argparse

parser = argparse.ArgumentParser(description="Meow like a Cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args( )

for _ in range(args.n):
    print("meow")