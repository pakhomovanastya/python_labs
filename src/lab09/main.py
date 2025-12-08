from group import Group
from lab08.models import Student

def main():
    # g = Group("../../data/lab_09/students_p.csv")
    # g.add(Student("Прудников Иван", "2000-01-01", "БИВТ-25-25", 2.3))

    g = Group("../../data/lab_09/students.csv")
    # print(g.find('ров'))
    # print(g.list())
    # g.add(Student("Прудников Иван", "2000-01-01", "БИВТ-25-25", 2.3))
    # print(g.find('ров'))
    # g.remove("Сидоров Андрей")
    # g.update("Сидоров Андрей", group="БИВТ-21-3", gpa=4.6)

if __name__ == '__main__':
    main()
    