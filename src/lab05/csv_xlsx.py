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
    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            people = csv.reader(f)
            people = list(people)
    except FileNotFoundError:
        raise FileNotFoundError("Осутствующий файл")
    if not people:
        raise ValueError('Пустой CSV')
    headers = people[0]
    if not headers:
        raise ValueError('Пустой заголовок в CSV')
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    for p in people:
        ws.append(p)
    for col in ws.columns:
        max_len = max(len(str(cell.value or "")) for cell in col)
    ws.column_dimensions[col[0].column_letter].width = max(max_len + 2, 8)
    wb.save(xlsx_path)
    
csv_to_xlsx(r"GitHub\python_labs\src\data\lab_05\people.csv", r"GitHub\python_labs\src\data\lab_05\people.xlsx")