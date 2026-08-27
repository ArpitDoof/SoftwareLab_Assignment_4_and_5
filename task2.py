import csv
from pathlib import Path
name = Path("students.csv")
# print(type(name))

if name.is_file():
    print("CSV file exists")

    with open(name,"r",newline="") as file:
        reader = csv.DictReader(file)
        students = list(reader)
    print(f"number of files present {len(students)}")

    csestudents = sum(student["Department"] == "CSE" for student in students)
    print(f"Number of students belonging to CSE are {csestudents}")

    ece = sum(student["Department"] == "ECE" for student in students)
    print(f"Number of students in ECE are {ece}")

    print("Analysis Completed")

else:
    print("No such file found")

