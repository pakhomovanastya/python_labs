import csv
from pathlib import Path
import sys
sys.path.append(r"C:\Users\First\Documents\GitHub\python_labs\src")
from lab08.models import Student

class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        if not self.path.exists():
            self.path.write_text("fio,birthdate,group,gpa\n", encoding="utf-8") 

    def _read_all(self): #список словарей
        '''прочитать все строки из CSV'''
        rows = []
        with open(self.path, "r", encoding="utf-8") as fr:
            csv_reader = csv.DictReader(fr, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            next(csv_reader) #пропустить первую строку

            for row in csv_reader:
                rows.append(row)
        return rows

    def list(self):
        '''вернуть всех студентов в виде списка Student'''
        students = []
        for s_dict in self._read_all():
            students.append(Student(s_dict['fio'], s_dict['birthdate'],s_dict ['group'], float(s_dict['gpa'])))
        return students

    def add(self, student: Student):
        '''добавить нового студента в CSV'''
        with open(self.path, "a", newline='',encoding="utf-8") as fw:
            writer = csv.DictWriter(fw, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writerow(student.to_dict())

    def find(self, substr: str):
        '''найти студентов по подстроке в fio'''
        rows = self._read_all()
        return [r for r in rows if substr in r["fio"]]  

    def remove(self, fio: str):
        '''удалить запись(и) с данным fio'''
        rows = self._read_all()
        for i, r in enumerate(rows):
            if r["fio"] == fio:
                rows.pop(i)
                break
        with open(self.path, "w", newline="", encoding="utf-8") as fw:
            writer_csv = csv.DictWriter(fw, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer_csv.writeheader()
            writer_csv.writerows(rows)

    def update(self, fio: str, **fields):
        '''обновить поля существующего студента'''
        rows = self._read_all()
        for r in rows:
            if r["fio"] == fio:
                for k, v in fields.items():
                    r[k] = v #в списке словарей где значение заменяем на другое
        with open(self.path, "w", newline="", encoding="utf-8") as fw:
            writer_csv = csv.DictWriter(fw, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer_csv.writeheader()
            writer_csv.writerows(rows)
        