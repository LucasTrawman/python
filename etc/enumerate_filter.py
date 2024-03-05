students = ["Harry", "Hermione", "Ron"]

gryffindors1 = [
    {"name": student, "house": "Gryffindor"} for student in students
]

print(gryffindors1)

gryffindors2 = {student: "Gryffindor" for student in students}

print("")
print(gryffindors2)

####################### Enumerate Function #######################
print("")
for i, student in enumerate(students):
    print(i + 1, student)