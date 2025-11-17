import argparse
import sys
sys.path.append(r'C:\Users\First\Documents\GitHub\python_labs\src')
from lab03.text_stats import analyze_text

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
    
def main():
    """Создаем основной парсер аргументов с описанием"""

    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    # Добавляем подпарсеры для поддержки подкоманд (cat, stats)
    # dest="command" означает, что выбранная команда будет сохранена в args.command
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Относительнаый(абсолютный) путь до файла")
    # Добавляем флаг -n (store_true означает, что если флаг присутствует - значение True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Относительнаый(абсолютный) путь до файла")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество самых частых слов")
    try:
        args = parser.parse_args()

        if args.command == "cat":
            """ Реализация команды cat """
            cat(args.input, args.n)
        elif args.command == "stats":
            """ Реализация команды stats """

            with open(args.input, 'r', encoding='utf-8') as fr:
                analyze_text(fr.read(), args.top) 
    except FileNotFoundError:
        print(f"FileNotFoundError: Отсутствие входного файла {args.input}")
    
    # Обрабатываем системный выход (когда пользователь вызывает --help или ошибки аргументов)
    except SystemExit:
        print("\nИсправьте аргументы и попробуйте снова")
        sys.exit(1)

if __name__=="__main__":
    main()