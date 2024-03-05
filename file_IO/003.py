import sys
import csv

if(len(sys.argv) != 3):
    sys.exit("Not the right number of arguments")

list = []

with open(sys.argv[1], "r") as file:
    reader = csv.DictReader(file)
    with open(sys.argv[2], "a") as file1:
        writer = csv.DictWriter(file1, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for line in reader:
            last, first = line["name"].split(",")
            last = last.strip()
            first = first.strip()
            writer.writerow({"house": line["house"], "first": first, "last": last})

with open(sys.argv[2], "r") as file:
    for line in file:
        reader = csv.DictReader(file)