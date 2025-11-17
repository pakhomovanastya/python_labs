Лабораторная работа №6
=
Модуль src/lab06/cli_text.py с подкомандами:
-
Импорты и настройка пути:
---
>argparse - стандартная библиотека для разбора аргументов командной строки
>sys.path.append() - добавляет путь к вашим модулям, чтобы Python мог найти lab03.text_stats

 ```python
 import argparse
import sys
sys.path.append(r'C:\Users\First\Documents\GitHub\python_labs\src')
from lab03.text_stats import analyze_text
 ```

Функция cat()
>fpath: str указывает что путь - строка, numeration: bool - булево значение
>Контекстный менеджер: with open(...) as fr гарантирует закрытие файла даже при ошибках
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
>add_subparsers() - позволяет создавать подкоманды (как в git: git commit, git push)
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

![alt text](def_cat_cli_text.png)
![alt text](def_main_cli_text.png)







