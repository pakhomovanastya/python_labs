import re
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold() 
        '''casefold() лучше чем lower(), потому что корректно работает с разными языками'''
    if yo2e:
        text = text.replace('Ё', 'Е')
        text = text.replace('ё', 'е')
    text = text.strip()
    text = re.sub(r'\\[trnwfdv]', ' ', text)
    '''Находит символы типа \t, \n, \r и заменяет их на обычные пробелы.
    Эти символы используются для переносов строк, табуляции и т.д.'''
    text = ' '.join(text.split())
    return text

def tokenize(text: str) -> list[str]:
    text_1 = text.replace(',', ' ').replace('.', ' ').replace(':', ' ').replace(';', ' ').replace('!', ' ').replace('?', ' ')
    text_1 = text_1.split()
    b = []
    for i in text_1:
        if i[0].isdigit() == 0 and i[0].isalpha() == 0: 
            pass ## Если первый символ "плохой" (например, смайлик), слово пропускается
        # i[0]== 0 тк мы проверяем являеться ли i числом\буквой,
        # 0 проверяет правда это или нет. Если fals, то не добавляем 
        # в список. pass пропускает i и не выполняет if
        else:
            b.append(i)
    return b

def count_freq(tokens: list[str]) -> dict[str, int]:
    unic_tokens = list(set(tokens))
    '''превращает это множество обратно в список,
    далее получаем список всех уникальных слов'''
    count_tokens = []
    for i in unic_tokens:
        count_tokens.append(tokens.count(i))
    dict_tokens = dict(zip(unic_tokens,count_tokens))
    '''"сшивает" два списка вместе [("a", 3), ("b", 2), ("c", 1)]
    dict(...) - превращает эти пары в словарь {"a": 3, "b": 2, "c": 1}'''
    return dict_tokens

# def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
#     freq = count_freq(freq)
#     new_dict = freq.items()
#     top = sorted(new_dict, key=lambda x: x[0])
#     '''мы сортируем список new_dict по параметру (x[0]) с помощью key
#     в key мы передаём пармаетр сортировка'''
#     ans = sorted(top, key=lambda x: -x[1])[:n]
#     return ans

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    freq = count_freq(freq)
    top = sorted(list(freq.items()), key=lambda x: (-x[1], x[0])) [:n] # items выводит список кортежей в формате (ключ, значение) 
    '''key=lambda x: x[0] правило сортировки и [:n] срез, берем только первые n элементов
    lambda x - создаем функцию
    (-x[1], x[0]) - кортеж из двух элементов:
    -x[1] - минус перед количеством (сортировка по частоты)
    x[0] - слово (сортировка по алфавита)
    далее сортируем слова по возрастанию'''
    return top

test_case_normalize = ['ПрИвЕт\nМИр\t', 'ёжик, Ёлка', 'Hello\r\nWorld', '  двойные   пробелы  ']
test_case_tokenize = ['привет мир', 'hello,world!!!', 'по-настоящему круто', '2025 год', 'emoji 😀 не слово']
test_case_count_freq =[["a","b","a","c","b","a"]]


for i in test_case_normalize:
    print(normalize(i))

for n in test_case_tokenize:
    print(tokenize(n))

for n in test_case_count_freq:
    print(top_n(n))