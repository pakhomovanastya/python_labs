from datetime import datetime, date #работает с датой и временем
from dataclasses import dataclass # библиотека для сереализации (есть некий объект и хотим превратить в текст)
@dataclass # декоратор - это то что будет выполнено до исполнения(заранее)
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self): #выполняется после создания объекта(вызова) конструктора
        if self.gpa > 5 or self.gpa < 0:
            raise ValueError("Неправильный gpa")
        try:
            self.birthdate = datetime.strptime(self.birthdate, "%Y-%m-%d") #%Y - год /%m - месяц /%d - дата
            #strptime преобразование строки к объекту datetime
        except ValueError:
            raise ValueError("Неправильная валидация даты")

    def age(self) -> int:
        b = self.birthdate
        today = date.today()
        if today.month > b.month:
            return today.year - b.year
        if today.month < b.month:
            return today.year - b.year - 1
        if today.day >= b.day:
            return today.year - b.year
        return today.year - b.year - 1

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate.strftime("%Y-%m-%d"),
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod # декоратор для класса, а не для объектта (можно вызывать от класса)
    def from_dict(cls, d: dict):
        fio = d["fio"]
        birthdate = d["birthdate"]
        group = d["group"]
        gpa = d["gpa"]
        return cls(fio, birthdate, group, gpa)

    def __str__(self):
        return f"Student:{self.fio}, {self.age()} years old, group {self.group}, rating {self.gpa}"
