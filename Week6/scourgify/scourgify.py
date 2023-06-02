import sys, csv, os.path


students = []


def main():
    if len(sys.argv) <= 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not os.path.isfile(sys.argv[1]):
        sys.exit(f"Could not read {sys.argv[1]}")
    else:
        with open(sys.argv[1], "r") as file:
            read = csv.DictReader(file)
            for row in read:
                x = list(row.keys())
                y = list(row.values())
                z = y[0].split(",")
                students.append(
                    {"first": z[1].strip(), "last": z[0].strip(), "house": y[1]}
                )
        with open(sys.argv[2], "w") as file2:
            write = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
            write.writeheader()
            for student in sorted(students, key=lambda student: student["first"]):
                write.writerow(student)


if __name__ == "__main__":
    main()
