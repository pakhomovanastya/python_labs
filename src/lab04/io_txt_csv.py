import csv #стандартный модуль Python для работы с CSV файлами
import os #для работы с операционной системой (создание папок)
from pathlib import Path
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    '''path - может быть строкой или объектом Path (путь к файлу)
    encoding - кодировка файла, по умолчанию "utf-8"
    -> str - функция возвращает строку'''
    p = Path(path)
    try:
        return p.read_text(encoding=encoding)
    #читаем весь файл как одну строку в указанной кодировке
    except FileNotFoundError:
        print(f'Ошибка: Файл {p} не найден.')
        return None
    except UnicodeDecodeError:
        print(f'Ошибка: Неверная кодировка. Должна быть {encoding}.')
        return None

def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    '''rows - итерируемый объект (можно перебирать) содержащий последовательности
    (строки, списки, кортежи)
    path - куда сохранить CSV файл
    header - заголовок таблицы, может быть None (без заголовка)'''
    p = Path(path)
    rows = list(rows) #преобразуем rows в список чтобы можно было несколько раз работать с данными
    with p.open("w", newline="", encoding="utf-8") as f:
        '''with - контекстный менеджер (автоматически закроет файл)
        "w" - открываем для записи (перезапишет если файл существует)
        newline=="" - настройка для корректной работы с CSV'''
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        else:
            header = ['Слово','Частота']
            w.writerow(header)
        for r in rows: 
            if len(r) == len(header):
                w.writerow(r)
                #для каждой строки в rows проверяем что ее длина совпадает с длиной заголовка
            else:
                raise ValueError('Разная длина строк.')
            
def ensure_parent_dir(path: str | Path) -> None: # принимает путь, ничего не возвращает
    parent_directory = os.path.dirname(path)
    # получение родительской директории: os.path.dirname() возвращает путь к папке где лежит файл
    os.makedirs(parent_directory, exist_ok=True)
    # os.makedirs() - создает все папки в пути
    # exist_ok==True - если папки уже существуют, не вызывает ошибку


def main():
    # txt = read_text("../data/input.txt") # относительный путь
    # print(txt)
    # print('пустой файл:', read_text(r"C:\Users\First\Documents\GitHub\python_labs\src\data\empty.txt"))
    print(read_text(r"C:\Users\First\Documents\GitHub\python_labs\src\data\input.txt"))
    write_csv([("word","count"),("test",3)], r"C:\Users\First\Documents\GitHub\python_labs\src\data\check.csv") 
    write_csv(rows=[], path=r"C:\Users\First\Documents\GitHub\python_labs\src\data\check_empty.csv", header=None) 

if __name__ == '__main__':
    main()
'''if __name__ == '__main__': - код выполнится только 
если файл запущен напрямую
Читаем разные файлы, пробуем записать CSV'''