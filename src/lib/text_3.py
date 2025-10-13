import re
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('Ё', 'Е')
        text = text.replace('ё', 'е')
    text = text.strip()
    text = re.sub(r'\\[trnwfdv]', ' ', text)
    text = ' '.join(text.split())
    return text

def tokenize(text: str) -> list[str]:
    a = re.findall(r'\w+(?:-\w+)*',text)
    return a

# def tokenize(text: str) -> list[str]:
#     text_1 = text.replace(',', ' ').replace('.', ' ').replace(':', ' ').replace(';', ' ').replace('!', ' ').replace('?', ' ')
#     text_1 = text_1.split()
#     b = []
#     for i in text_1:
#         if i[0].isdigit() == 0 and i[0].isalpha() == 0: pass #i[0]== 0 тк мы проверяем являеться ли i числом\буквой,
#             #0 проверяет правда это или нет. Если fals, то не добавляем в список. pass пропускает i и не выполняет if
#         else:
#             b.append(i)
#     return b

def count_freq(tokens: list[str]) -> dict[str, int]:
    unic_tokens = list(set(tokens))
    count_tokens = []
    for i in unic_tokens:
        count_tokens.append(tokens.count(i))
    dict_tokens = dict(zip(unic_tokens,count_tokens))
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
    return top

