Лабораторная работа №8
=
lab08/models.py:
-
Тестирование функции normalize()
>Модуль содержит определение класса Student для представления студента.
>
>Использует декоратор @dataclass для автоматической генерации методов.
 ```python
from datetime import datetime, date
from dataclasses import dataclass
```

>Класс, представляющий студента учебного заведения.
>Атрибуты:
>
>fio (str): ФИО студента в формате "Фамилия Имя"
>
>birthdate (str): Дата рождения в строковом формате
>
>group (str): Учебная группа студента
>
>gpa (float): Средний балл успеваемости
>
>Методы:
>age(): Рассчитывает возраст студента
>
>to_dict(): Преобразует объект в словарь
>
>from_dict(): Создает объект из словаря
>
>__str__(): Возвращает строковое представление
```python
@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __init__(self, fio, birthdate, group, gpa):
        """
        Конструктор класса Student.
        
        Args:
            fio (str): ФИО студента
            birthdate (str): Дата рождения (YYYY/MM/DD)
            group (str): Учебная группа
            gpa (float): Средний балл
            
        Note:
            Явно определенный конструктор позволяет вызвать __post_init__
            для валидации данных после инициализации.
        """
        self.fio = fio
        self.birthdate = birthdate
        self.group = group
        self.gpa = gpa
        self.__post_init__()
```

>Метод, автоматически вызываемый после __init__.
>Выполняет валидацию данных.
>       
>Raises:
>ValueError: При некорректном GPA или формате даты
>           
>Валидация включает:
>1. Проверку GPA в диапазоне 0-5
>2. Проверку формата даты (YYYY/MM/DD)

```python
def __post_init__(self):
    # Валидация GPA
    if self.gpa > 5 or self.gpa < 0:
        raise ValueError("Неправильный gpa")
        
    # Валидация формата даты
    try:
        # Преобразуем строку в объект datetime для проверки формата
        # %Y - год (4 цифры), %m - месяц, %d - день
        self.birthdate = datetime.strptime(self.birthdate, "%Y/%m/%d")
    except ValueError:
        raise ValueError("Неправильный формат даты рождения, ожидается:ГГГГ-ММ-ДД")
```

>Рассчитывает возраст студента в полных годах.
>
>Returns:
>>int: Возраст студента на текущую дату
>
>Алгоритм:
>>1. Сравнивает текущий месяц с месяцем рождения
>>2. Если текущий месяц больше - возраст = разница лет
>>3. Если текущий месяц меньше - возраст = разница лет - 1
>>4. Если месяцы равны - сравнивает дни

```python
def age(self) -> int:
    b = self.birthdate  # birthdate теперь объект datetime после валидации
    today = date.today()
    
    if today.month > b.month:
        return today.year - b.year
    if today.month < b.month:
        return today.year - b.year - 1
    if today.day >= b.day:
        return today.year - b.year
    return today.year - b.year - 1
```


>Сериализует объект Student в словарь.
>Returns:
>    dict: Словарь с данными студента, готовый для JSON-сериализации 
>Структура словаря:
{
    "fio": "ФИО",
    "birthdate": "дата в формате YYYY/MM/DD",
    "group": "группа",
    "gpa": балл
}
```python
def to_dict(self) -> dict:
    return {
        "fio": self.fio,
        "birthdate": self.birthdate.strftime("%Y/%m/%d"),  # Преобразуем обратно в строку
        "group": self.group,
        "gpa": self.gpa,
    }
```


>Десериализует словарь в объект Student.
>
>Args:
>    d (dict): Словарь с данными студента
>    
>Returns:
>    Student: Новый объект класса Student
>    
>Note:
>    Используется как фабричный метод (classmethod)
```python
@classmethod 
def from_dict(cls, d: dict):
    fio = d["fio"]
    birthdate = d["birthdate"]
    group = d["group"]
    gpa = d["gpa"]
    return cls(fio, birthdate, group, gpa)
```

>Возвращает читаемое строковое представление объекта.
>
>Returns:
>    str: Форматированная строка с информацией о студенте
```python
def __str__(self):
    return f"Student:{self.fio}, {self.age()} years old, group {self.group}, rating {self.gpa}"
```
 

lab08/serialize.py
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
import json
from models import Student
def students_to_json(students, path):
    # Преобразуем список объектов в список словарей
    data = [s.to_dict() for s in students]
    
    # Открываем файл для записи с кодировкой UTF-8
    with open(path, "w", encoding="utf-8") as fw:
        # Записываем данные в JSON формате
        # ensure_ascii=False - сохраняет кириллицу как есть
        # indent=2 - добавляет отступы для читаемости
        fw.write(json.dumps(data, ensure_ascii=False, indent=2))
```

>Загружает список объектов Student из JSON файла.
>Args:
>    path (str): Путь к JSON файлу
>        
>Returns:
>    list[Student]: Список объектов Student
>        
>Process:
>1. Читает JSON файл
>2. Преобразует JSON в список словарей
>3. Создает объекты Student из каждого словаря
```python
def students_from_json(path):
    # Открываем файл для чтения с кодировкой UTF-8
    with open(path, "r", encoding="utf-8") as fr:
        # Загружаем JSON данные из файла
        data = json.load(fr)
    
    # Преобразуем каждый словарь в объект Student
    return [Student.from_dict(d) for d in data]
```

lab08/main.py
-

>Основной модуль для демонстрации работы с классом Student.
>Содержит примеры использования всех методов.
>
>Демонстрирует:
>1. Создание объектов Student
>2. Сериализацию в JSON файл
>3. Десериализацию из JSON файла
>4. Вывод информации о студентах
```python
from serialize import students_from_json, students_to_json
from models import Student

def main():
    # 1. СОЗДАНИЕ ОБЪЕКТОВ STUDENT
    # Каждый объект проходит валидацию в __post_init__()
    s1 = Student("John Snow", "2000/12/1", "SE-01", 4.3)
    s2 = Student("Michael Jordan", "1975/11/11", "PP-01", 5.0)
    s3 = Student("John Smit", "1992/2/14", "JJ-92", 3.1)
    # 2. СЕРИАЛИЗАЦИЯ В JSON
    # Преобразуем список объектов в JSON файл
    students_to_json([s1, s2, s3], "../../data/lab_08/students_output.json")
    
    # 3. ДЕСЕРИАЛИЗАЦИЯ ИЗ JSON
    # Загружаем данные из JSON файла и создаем объекты
    loaded_students = students_from_json("../../data/lab_08/students_input.json")
    
    # 4. ВЫВОД ИНФОРМАЦИИ
    # Демонстрация работы метода __str__()
    for s in loaded_students:
        print(s)

if __name__ == '__main__':
    main()
```
lab08/models.py
-
<img width="1383" height="911" alt="models-1" src="https://github.com/user-attachments/assets/cbfcd2cb-2258-4d86-829e-3f03081cc84c" />
<img width="1117" height="901" alt="models-2" src="https://github.com/user-attachments/assets/f5c2883c-9966-4ea2-bed9-5f9626582fc3" />

lab08/serialize.py
-
<img width="1012" height="330" alt="serialize" src="https://github.com/user-attachments/assets/9ae47bf0-a1ea-40b6-bf73-f54469554056" />

lab08/main.py
-
<img width="837" height="362" alt="main" src="https://github.com/user-attachments/assets/146d2df9-5a5b-4052-a388-6dcf16bef9f5" />

Пример вывода программы
-
<img width="720" height="197" alt="вывод" src="https://github.com/user-attachments/assets/d43e8dd8-10a0-438f-81b2-3cec4f73329f" />
