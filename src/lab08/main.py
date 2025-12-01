from serialize import students_from_json, students_to_json
from models import Student

def main():
    s1 = Student("John Snow","2000/12/1", "SE-01", 4.3)
    s2 = Student("Michael Jordan","1975/11/11", "PP-01", 5.0)
    s3 = Student("John Smit","1992/2/14", "JJ-92", 3.1)
    students_to_json([s1,s2,s3], "../../data/lab_08/students_output.json")
    for s in students_from_json("../../data/lab_08/students_input.json"):
        print(s)
    # print(s1)
    # s1_dict = s1.to_dict()
    # print(Student.from_dict(s1_dict))
    # print(Student.from_dict({
    #     'fio': 'John Snow', 
    #     'birthdate': datetime.datetime(2000, 12, 1, 0, 0), 
    #     'group': 'SE-01', 
    #     'gpa': 4.3
    # }))



if __name__ == '__main__':
    main()