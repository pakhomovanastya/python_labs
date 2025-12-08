import json
from .models import Student

def students_to_json(students, path):
    """Сохраняет список объектов Student в JSON файл"""
    data = [s.to_dict() for s in students] #от объекта вызываем to_dict
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path):
    """Загружает список объектов Student из JSON файла"""
    result = []
    with open(path, "r", encoding="utf-8") as f:
        students = json.load(f) 
        for s in students:
            result.append(Student.from_dict(s)) #от класса вызываем from_dict
    return result
