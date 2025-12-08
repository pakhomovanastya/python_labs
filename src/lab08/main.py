from .serialize import students_to_json, students_from_json
from .models import Student


def input_students_from_json(src):
    studentiki = students_from_json(src)
    for s in studentiki:
        print(s) 
input_students_from_json("../data/lab_08/students_input.json")

def output_students_to_json(src):
    s1 = Student("Maria R", "2004-03-07", "II-09", 4.8)
    s2 = Student("Bob S", "2009-04-14", "SE-05", 3.2)
    s3 = Student("Carl M", "2006-06-25", "G-11", 4.3)
    stud = [s1, s2, s3]
    students_to_json(stud, src)
output_students_to_json("../data/lab_08/students_output.json")
