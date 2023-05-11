# students = ["Herione", "Harry", "Ron"]

# # for i in range(len(students)):
# #     print(f"Hello, {students[i]} you are the number {i + 1} student in your class")

# houses = ["Gryffidor", "Gryffidor", "Gryffidor", "Slytherin"]

# students = {
#     "Hermione": "Gryffidor",
#     "Harry": "Gryffidor",
#     "Ron": "Gryffidor",
#     "Draco": "Slytherin",
# }

# for student in students:
#     print(student, students[student], sep=", ")


students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Hermione", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
