from pathlib import Path
import json
import csv
def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    json_path = Path(json_path)
    if json_path.suffix.casefold() != ".json": 
        raise ValueError('Неверный тип файла для аргумента json_path') 
    

    try:
        with open(json_path , encoding="utf-8") as f:
            people = json.load(f) #загрузить из файла
    except json.decoder.JSONDecodeError:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    
    for p in people:
        if type(p)!=dict: #записать в файл
            raise ValueError("Список с не-словарами")
        
    with open(csv_path,'w', newline="",encoding="utf-8" ) as f:
        writer_csv = csv.DictWriter(f, people[0].keys())
        writer_csv.writeheader()
        writer_csv.writerows(people)
        
    
def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    csv_path = Path(csv_path)
    if csv_path.suffix.casefold() != ".csv": 
        raise ValueError('Неверный тип файла для аргумента csv_path')

    try:
        with open(csv_path , encoding="utf-8") as f:
            people = csv.DictReader(f) #читает CSV как список словарей
            rows = list(people)
    except :
        raise FileNotFoundError("Осутствующий файл")
    
    if not rows:
        raise ValueError("Пустой CSV")
    
    if not people.fieldnames:
        raise ValueError("CSV без заголовка")
    
    with open(json_path,'w', encoding="utf-8" ) as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)

json_to_csv("data/samples/people.json", "data/out/people_from_json.csv") #относительной путь онтосительно этого файла
csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")
