class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House ")
        return cls(name, house)

    # def charm(self):
    #     match self.patronus:
    #         case "Stag":
    #             return "🐐"
    #         case "Otter":
    #             return "🐠"
    #         case "Jack Russell terrier":
    #             return "🐶"
    #         case _:
    #             return "🪄"

    # @property
    # def name(self):
    #     return self._name

    # @name.setter
    # def name(self, name):
    #     if not name:
    #         raise ValueError("Missing name")
    #     self._name = name

    # @property
    # def house(self):
    #     return self._house

    # @house.setter
    # def house(self, house):
    #     if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
    #         raise ValueError("Invalid house")
    #     self._house = house


def main():
    student = Student.get()
    # if student[0] == "Padma":
    #     student[1] = "Ravenclaw"
    # if student["name"] == "Padma":
    #     student["house"] = "Ravenclaw"
    # print(f"{student.name} from {student.house}")
    # print("Expecto Patronum!")
    print(student)


# Tuples are immutable
# Use a list to be able to update values

# def get_name():
#     return input("Name: ")


# def get_house():
#     return input("House: ")


# def get_student():
#     # name = input("Name: ")
#     # house = input("House: ")
#     # return [name, house]
#     # student = {}
#     # student["name"] = input("Name: ")
#     # student["house"] = input("House: ")
#     # return student
#     # name = input("Name: ")
#     # house = input("House: ")
#     # return {"name": name, "house": house}
#     # student = Student()
#     # student.name = input("Name: ")
#     # student.house = input("House: ")
#     name = input("Name: ")
#     house = input("House: ")
#     # patronus = input("Patronus: ")
#     return Student(name, house)


if __name__ == "__main__":
    main()
