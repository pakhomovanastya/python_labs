Лабораторная работа №6
=
cli_text.py с подкомандами:
-
Импорты и настройка пути:
---
>argparse - стандартная библиотека для разбора аргументов командной строки
>
>sys.path.append() - добавляет путь к вашим модулям, чтобы Python мог найти lab03.text_stats

 ```python
 import argparse
import sys
sys.path.append(r'C:\Users\First\Documents\GitHub\python_labs\src')
from lab03.text_stats import analyze_text
 ```

Функция cat()
>fpath: str указывает что путь - строка, numeration: bool - булево значение
>
>Контекстный менеджер: with open(...) as fr гарантирует закрытие файла даже при ошибках
>
>enumerate: генерирует пары (номер, элемент) начиная с указанного числа (1)

```python
def cat(fpath: str , numeration: bool) -> None:
    """Функция для вывода содержимого файла с номерами строк или без"""

    with open(fpath, 'r', encoding="utf-8") as fr:
        if numeration:
            # Если включена нумерация строк
            for i, line in enumerate(fr.readlines(), 1): 
                # enumerate превращает в пары (номер, элемент коллекции), начиная с 1
                # strip() удаляет лишние пробелы и переводы строк в начале и конце
                print(f'{i}: {line.strip()}')
        else:
            #Если нумерация отключена - просто выводим строки
            for line in fr.readlines():
                print(line.strip())
```

Создание парсера аргументов
>ArgumentParser - главный объект для обработки аргументов
>
>add_subparsers() - позволяет создавать подкоманды (как в git: git commit, git push)
>
>dest="command" - выбранная команда сохранится в args.command

Добавление аргументов
```python
cat_parser.add_argument("--input", required=True, help="Описание")
```
>--input - длинное имя аргумента (можно использовать -i для короткого)
>required=True - аргумент обязателен для указания
>help - текст справки, показывается при --help

```python
cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")
```
>-n - короткое имя флага
>action="store_true" - если флаг указан, значение становится True, иначе False

Команда cat:
>Без нумерации

>С нумерацией строк

Команда stats:
>Топ 5 слов (по умолчанию)

>Топ 10 слов

код cli_convert.py
---
Структура подкоманд
>Создает систему подкоманд, аналогичную git: git commit, git push
>
>dest="cmd" - выбранная команда сохраняется в переменную args.cmd
```python
sub = parser.add_subparsers(dest="cmd")
```

Особенность аргументов --in и --out
>--in - имя аргумента в командной строке
>
>dest="input" - внутреннее имя переменной (чтобы использовать args.input вместо args.in)
>
>Это полезно потому что in - ключевое слово в Python
```python
p1.add_argument("--in", dest="input", required=True, help="Входной файл json")
```

Обработка исключений
>Возникает когда указанный файл не существует
>
>Выводит понятное сообщение об ошибке
```python
except FileNotFoundError:
    print(f"FileNotFoundError: Отсутствие входного файла {args.input}")
```

SystemExit
>argparse.parse_args() вызывает sys.exit() при --help или ошибках аргументов
>
>Перехватываем это чтобы вывести более дружелюбное сообщение
>
>sys.exit(1) - завершаем с кодом ошибки (1 = ошибка, 0 = успех)
```python
except SystemExit:
    print("\nИсправьте аргументы и попробуйте снова")
    sys.exit(1)
```

Конвертация JSON в CSV:
```
python .\cli_convert.py json2csv --in "..\..\data\samples\people.json" --out "..\..\data\out\people_06.csv"
```

Конвертация CSV в JSON:
```
python .\cli_convert.py csv2json --in "..\..\data\samples\people.csv" --out "..\..\data\out\people_06.json"
```

Конвертация CSV в XLSX:
```
python .\cli_convert.py csv2xlsx --in "..\..\data\samples\people.csv" --out "..\..\data\out\people_06.xlsx"
```