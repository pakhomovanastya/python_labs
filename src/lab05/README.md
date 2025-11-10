Лабораторная работа №5
=
Задание A — JSON ↔ CSV
-
Функция json_to_csv:
---
Открываем и читаем JSON-файл
>with open(...) — безопасно открываем файл (автоматически закроется)
>json.load(f) — превращаем текст из файла в структуры данных Python
>Если файл поврежден — выдаем ошибку "Пустой JSON..."

>Проверяем, что данные правильные
>Проходим по всем элементам списка for p in people
>Проверяем, что каждый элемент — словарь type(p) != dict
>Если нашли не словарь (например, число или строку) — выдаем ошибку

Записываем CSV-файл
>csv.DictWriter — специальный писатель, который понимает словари
>people[0].keys() — берем названия колонок из первого словаря
>writeheader() — записываем строку с названиями колонок
>writerows(people) — записываем все данные сразу
 ```
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
        writer_csv = csv.DictWriter(f, people[0].keys())
        writer_csv.writeheader()
        writer_csv.writerows(people)
```

Функция csv_to_json
---
Читаем CSV-файл
>csv.DictReader(f) — читает CSV и сразу превращает каждую строку в словарь
>Ключи словаря — названия колонок, значения — данные ячеек
>list(people) — превращаем все строки в список словарей

Проверяем данные
>if not rows — если список пустой, значит CSV без данных
>if not people.fieldnames — если нет названий колонок

Записываем JSON
>json.dump(rows, f, ...) — превращаем список словарей в JSON-текст
>ensure_ascii=False — разрешаем русские буквы
>indent=2 — красивое форматирование с отступами
 ```
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

json_to_csv("data/samples/people.json", "data/out/people_from_json.csv") #относительной путь онтосительно этого файла
csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")

 ```

Задание B — CSV → XLSX
-
Функция csv_to_xlsx
---

Проверяем расширения файлов
>Path(xlsx_path).suffix — получаем расширение файла (.xlsx, .csv)
>casefold() — игнорируем регистр (.XLSX тоже подойдет)
>Проверяем, что файлы правильного типа

Читаем CSV-файл
>csv.reader(f) — читаем CSV построчно
>list(people) — превращаем все строки в список

Проверяем данные
>Если список пустой — ошибка
>Проверяем, что вторая колонка заголовка — не число (простая проверка на заголовок)

Создаем Excel-книгу
>Workbook() — создаем новую Excel-книгу
>wb.active — получаем активный лист
>ws.title = "Sheet1" — даем листу имя

Записываем данные
>for p in people: — проходим по всем строкам CSV
>ws.append(p) — добавляем строку в Excel

Настраиваем ширину колонок
>for col in ws.columns: — проходим по всем колонкам Excel
>max(len(str(cell.value or "")) for cell in col) — находим самую длинную строку в колонке
>max(max_len + 2, 8) — устанавливаем ширину: либо (макс.длина + 2), либо минимум 8 символов

Сохраняем файл
>wb.save(xlsx_path) — сохраняем Excel-файл
```
from pathlib import Path
import csv
from openpyxl import Workbook

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    xlsx_path = Path(xlsx_path) #преобразуем в объекты типа Path, чтобы мы работали с путями
    csv_path = Path(csv_path)
    if xlsx_path.suffix.casefold() != ".xlsx": 
        raise ValueError('Неверный тип файла для аргумента xlsx_path') 
    if csv_path.suffix.casefold() != ".csv": 
        raise ValueError('Неверный тип файла для аргумента csv_path')

    try: 
        with open(csv_path, "r", encoding="utf-8") as f: 
            people = csv.reader(f) 
            people = list(people)
    except FileNotFoundError:
        raise FileNotFoundError("Осутствующий файл")
    
    if not people:
        raise ValueError('Пустой CSV')
    
    headers = people[0]
    if headers[1].isdigit(): 
        #проверяем, что в первой строке 2го столбеца это число,
        #тогда выводится ошибка(т.к. это не заголовок)
        raise ValueError('Пустой заголовок в CSV')
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for p in people:
        ws.append(p) #сразу записываем построчно 

    for col in ws.columns: #цикл бежим по колонкам
        max_len = max(len(str(cell.value or "")) for cell in col) #макс длинна строки в колонке,преврати в строку, где пробежимся по всем значениям колонки, посмотри на длину в текущей колонке и возьми макс длину
        ws.column_dimensions[col[0].column_letter].width = max(max_len + 2, 8) #изменяем ширину текущей(каждой) колонки
    wb.save(xlsx_path)
    
csv_to_xlsx("data/samples/people.csv", "data/out/people_from_csv2.xlsx")
```

Сценарий запуска
-
>Мы находимся в папке lab05
>Нам нужно подняться на деррикторию выще cd .. к src
>Далее поднимаемся к папке python_labs cd .. , чтобы сохранить файлы в папку data
>Прописывем путь python .\src\lab05\json_csv.py и python .\src\lab05\csv_xlsx.py из папки lad05
>где сохраняться в папке data

<img width="1263" height="323" alt="запуск заданий А и В" src="https://github.com/user-attachments/assets/0c0acd2a-8a6e-47ce-b796-67e238aca96e" />




