#example of a structure with FOR and IF inside a list, so you can control what is going inside
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

#############################################################################

gryffindors1 = [
  student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors1):
    print(gryffindor)

print("")

#############################################################################

gryffindors2 = filter(lambda s: s["house"] == "Gryffindor", students)

for gryffindor in sorted(gryffindors2, key=lambda s: s["name"]):
    print(gryffindor["name"])