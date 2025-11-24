import sys

# sys.path.append(r'C:\Users\First\Documents\GitHub\python_labs\src\lib')
# добавляем путь к папке lib, чтобы Python мог найти наши модули

from .text import *

# импортируем ВСЕ функции из файла text_3.py


def analyze_text(text: str, n: int) -> None:
    """создаем функцию, которая принимает текст и ничего не возвращает"""
    print(f"Всего слов: {len(tokenize(normalize(text)))}")
    print(f"Уникальных слов: {len(count_freq(tokenize(normalize(text))))}")
    print(f"Топ-{n}:")
    for i in top_n(tokenize(normalize(text)), n):
        print(f"{i[0]}: {i[1]}")


def main():
    input_text = sys.stdin.buffer.read().decode("utf-8")
    """ читаем весь ввод из командной строки
    и преобразуем байты в нормальный текст"""
    analyze_text(input_text)


if __name__ == "__main__":
    main()
