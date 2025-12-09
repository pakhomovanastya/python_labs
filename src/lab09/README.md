Лабораторная работа №9
=
lab09/group.py

Класс Group
>Класс представляет собой менеджер для работы с данными студентов в CSV-файле.
>
Параметры:
storage_path - путь к CSV-файлу
>
Что делает:
>Преобразует строку пути в объект Path
>
>Проверяет существование файла
>
>Если файла нет - создает его с заголовками столбцов
>Возвращает: Объект класса Group
```python
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
    def __init__(self, storage_path: str):
    self.path = Path(storage_path)
    if not self.path.exists():
        self.path.write_text("fio,birthdate,group,gpa\n", encoding="utf-8") 

```

Метод _read_all()
>Назначение: Внутренний метод для чтения всех данных из CSV-файла
>
Что делает:
>Открывает файл для чтения в кодировке UTF-8
>
>Создает DictReader для чтения CSV как словарей
>
>Пропускает заголовок (первую строку)
>
>Читает все строки и добавляет их в список
>Возвращает: Список словарей с данными студентов
>Примечание: Метод начинается с _, что означает "внутренний/приватный"
```python
def _read_all(self): #список словарей
        '''прочитает весь файл и возвращает список словарей'''
        rows = []
        with open(self.path, "r", encoding="utf-8") as fr:
            csv_reader = csv.DictReader(fr, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            next(csv_reader) #пропустить первую строку

            for row in csv_reader:
                rows.append(row)
        return rows
```

Метод list()
>Назначение: Получить всех студентов как объекты класса Student
>
Что делает:
>Вызывает _read_all() для получения данных из файла
>
>Для каждой записи создает объект Student
>
>Преобразует GPA из строки в число с плавающей точкой
>Возвращает: Список объектов Student
>CRUD операция: Read (чтение)
```python
def list(self):
        '''преобразует записи из файла в список объектов Student'''
        students = []
        for s_dict in self._read_all():
            students.append(Student(s_dict['fio'], s_dict['birthdate'],s_dict ['group'], float(s_dict['gpa'])))
        return students
```

Метод add(student: Student)
>Назначение: Добавить нового студента в файл
Параметры:
>student - объект класса Student
>
Что делает:
>Открывает файл в режиме добавления ("a")
>
>Создает DictWriter для записи CSV
>
>Преобразует объект Student в словарь и записывает в файл
>CRUD операция: Create (создание)
```python
def add(self, student: Student):
        '''добавить нового студента в CSV'''
        with open(self.path, "a", newline='',encoding="utf-8") as fw:
            writer = csv.DictWriter(fw, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writerow(student.to_dict())
```

Метод find(substr: str)
>Назначение: Поиск студентов по подстроке в ФИО
>
Параметры:
>substr - подстрока для поиска
>
Что делает:
>Читает все данные из файла
>
>Использует list comprehension для фильтрации
>
>Ищет подстроку в поле "fio" каждого студента
>Возвращает: Список словарей с найденными студентами
>CRUD операция: Read (чтение с фильтрацией)
```python
def find(self, substr: str):
        '''найти студентов по подстроке в fio'''
        rows = self._read_all()
        return [r for r in rows if substr in r["fio"]]  
```

Метод remove(fio: str)
>Назначение: Удалить студента по точному совпадению ФИО
>
Параметры:
>fio - полное ФИО студента для удаления
>
Что делает:
>Читает все данные из файла
>
>Ищет запись с указанным ФИО
>
>Удаляет найденную запись из списка
>
>Перезаписывает весь файл с обновленными данными
>CRUD операция: Delete (удаление)
>Примечание: Удаляет только первое найденное совпадение
```python
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
```

Метод update(fio: str, **fields)
>Назначение: Обновить данные студента
>
Параметры:
>fio - ФИО студента для обновления
>
>**fields - произвольное количество полей для обновления
>
Что делает:
>Читает все данные из файла
>
>Ищет студента с указанным ФИО
>
>Обновляет указанные поля
>
>Перезаписывает весь файл
>CRUD операция: Update (обновление)
>Пример использования:
```python
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
```
 

lab09/main.py
-

>Модуль для сериализации и десериализации объектов Student в >формате JSON.
>Содержит функции для работы с файлами JSON.
>
>Сохраняет список объектов Student в JSON файл.
>Args:
>    students (list[Student]): Список объектов Student для сохранения
>    path (str): Путь к файлу для сохранения
>  
>Process:
>1. Преобразует каждый Student в словарь с помощью to_dict()
>2. Сохраняет список словарей в JSON файл
>3. Использует кодировку UTF-8 для поддержки кириллицы
>4. Форматирует JSON с отступами для читаемости
```python
from group import Group
from lab08.models import Student

def main():
    g = Group("../../data/lab_09/students.csv")
    # print(g.find('ров'))
    # print(g.list())
    # g.add(Student("Прудников Иван", "2000-01-01", "БИВТ-25-25", 2.3))
    # print(g.find('ров'))
    # g.remove("Сидоров Андрей")
    # g.update("Сидоров Андрей", group="БИВТ-21-3", gpa=4.6)

if __name__ == '__main__':
    main()
    
```

group.py
===
<img width="1197" height="691" alt="group_01" src="https://github.com/user-attachments/assets/d933bf67-03c5-45ff-9360-b71451f85716" />
<img width="1112" height="882" alt="group_02" src="https://github.com/user-attachments/assets/ef2de457-af0a-4d7f-b254-41e25bc5b8da" />

main.py
===

Добавление нового студента
>g.add(Student("Прудников Иван", "2000-01-01", "БИВТ-25-25", 2.3))
===
<img width="1481" height="622" alt="add" src="https://github.com/user-attachments/assets/e06d1be1-4048-4149-9442-7238df81213a" />


Поиск студентов
>print(g.find('ров'))  # Найдет всех с "ров" в имени
===
<img width="1473" height="688" alt="find" src="https://github.com/user-attachments/assets/1ba993ac-c879-4bfc-a0f4-f81249ef2eab" />


Получение списка всех студентов
>all_students = g.list()
===
<img width="1483" height="605" alt="list" src="https://github.com/user-attachments/assets/d9a67a9c-3c63-4f96-917b-330f9de08bd4" />


Удаление студента
>g.remove("Сидоров Андрей")
===
<img width="1475" height="753" alt="remove" src="https://github.com/user-attachments/assets/46b461d2-4bb4-4e52-9868-9987a53f62da" />

Обновление данных
>g.update("Сидоров Андрей", group="БИВТ-21-3", gpa=4.6)
===
<img width="1543" height="392" alt="update" src="https://github.com/user-attachments/assets/41980878-30ae-4a7e-b979-0b38b3d6bab9" />
