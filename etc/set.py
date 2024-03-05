students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]  

houses1 = []
for student in students:
    if student["house"] not in houses1:
        houses1.append(student["house"])

for house in sorted(houses1):
    print(house)
######### version with set() #########

houses2 = set()
for student in students:
    houses2.add(student["house"])

for house2 in sorted(houses2):
    print(house2)