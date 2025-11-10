import csv
import json
from pprint import pprint
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    json_path = Path(json_path) #преобразуем в объекты типа Path, чтобы мы работали с путями
    csv_path = Path(csv_path) 
    if json_path.suffix.casefold() != ".json": #расширение файла у нашего относительного пути
        raise ValueError('Неверный тип файла для аргумента json_path')
    if csv_path.suffix.casefold() != ".csv":
        raise ValueError('Неверный тип файла для аргумента csv_path')
    with open (json_path, "r", encoding='utf-8') as fr: #r для чтения файла
        data = json.load(fr) #список словарей, load метод загрузки из библиотеки json
        with open (csv_path, "w", encoding='utf-8', newline="") as fw:
            writer = csv.DictWriter(fw, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    json_path = Path(json_path) #преобразуем в объекты типа Path, чтобы мы работали с путями
    csv_path = Path(csv_path) 
    if json_path.suffix.casefold() != ".json": #расширение файла у нашего относительного пути
        raise ValueError('Неверный тип файла для аргумента json_path')
    if csv_path.suffix.casefold() != ".csv":
        raise ValueError('Неверный тип файла для аргумента csv_path')
    
    with open (csv_path, "r", encoding='utf-8') as fr: #r для чтения файла
        reader = csv.DictReader(fr) #объект
        data = list(reader) #не в виде объекта а преобразовать в список словарей для стандартной работы с данными
        
        with open (json_path, "w", encoding='utf-8') as fw:
            json.dump(data, fw, ensure_ascii=False, indent=2) #записать в файл;

json_to_csv("data/lab_05/people.json", "data/lab_05/people_from_json.csv") #относительной пусть онтосительно этого файла
csv_to_json("data/lab_05/people.csv", "data/lab_05/people_from_csv.json")
