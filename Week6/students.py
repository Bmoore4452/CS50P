# # with open("students.csv") as file:
# #     for line in file:
# #         name, city = line.rstrip().split(",")
# #         print(f"{name} is in {city}")
# import csv

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, city = line.rstrip().split(",")
#         student = {"name": name, "city": city}
#         students.append(student)


# def get_name(student):
#     return student["city"]


# for student in sorted(students, key=lambda student: student["city"]):
#     print(f"{student['name']} is from {student['city']}")

# lambda is an anonymous function

# for student in sorted(students):
#     print(student)

# import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "city": row["city"]})


# for student in sorted(students, key=lambda student: student["city"]):
#     print(f"{student['name']} is from {student['city']}")


import csv

name = input("What's your name? ")
city = input("What's the name of your city? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "city"])
    writer.writerow({"name": name, "city": city})

