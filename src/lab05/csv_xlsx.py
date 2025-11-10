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
        max_len = max(len(str(cell.value or "")) for cell in col) 
        #макс длинна строки в колонке,преврати в строку, где пробежимся по всем значениям колонки, 
        ##посмотри на длину в текущей колонке и возьми макс длину
        ws.column_dimensions[col[0].column_letter].width = max(max_len + 2, 8) #изменяем ширину текущей(каждой) колонки
    wb.save(xlsx_path)
    
csv_to_xlsx("samples/people.csv", "samples/people_from_csv2.xlsx")
