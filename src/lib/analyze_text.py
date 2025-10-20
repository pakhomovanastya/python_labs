import sys
sys.path.append(r'C:\Users\First\Documents\GitHub\python_labs\src\lib')
# добавляем путь к папке lib, чтобы Python мог найти наши модули

from text_3 import*
#импортируем ВСЕ функции из файла text_3.py

def analyze_text(text: str) -> None:
    '''создаем функцию, которая принимает текст и ничего не возвращает'''
    print(f'Всего слов: {len(tokenize(normalize(text)))}')
    print(f'Уникальных слов: {len(count_freq(tokenize(normalize(text))))}')
    print(f'Топ-5:')
    c = 0
    for i in top_n(tokenize(normalize(text))):
        c += 1
        if c == 5:
            break
        print(f'{i[0]}: {i[1]}')