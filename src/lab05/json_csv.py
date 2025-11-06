import json
import csv
def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    try:
        with open(json_path , encoding="utf-8") as f:
            people = json.load(f)
    except json.decoder.JSONDecodeError:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    for p in people:
        if type(p)!=dict:
            raise ValueError("Список с не-словарами")
    with open(csv_path,'w', newline="",encoding="utf-8" ) as f:
        # writer_csv = csv.DictWriter(f, ["name", "age", "city"])
        writer_csv = csv.DictWriter(f, people[0].keys())
        writer_csv.writeheader()
        writer_csv.writerows(people)
        
    
def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    try:
        with open(csv_path , encoding="utf-8") as f:
            people = csv.DictReader(f)
            rows = list(people)
    except :
        raise FileNotFoundError("Осутствующий файл")
    if not rows:
        raise ValueError("Пустой CSV")
    if not people.fieldnames:
        raise ValueError("CSV без заголовка")
    with open(json_path,'w', encoding="utf-8" ) as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)


# json_to_csv(r"GitHub\python_labs\src\data\lab_05\people.json", r"GitHub\python_labs\src\data\lab_05\people_from_json.csv")
# csv_to_json(r"GitHub\python_labs\src\data\lab_05\people.csv", r"GitHub\python_labs\src\data\lab_05\people_from_csv.json")