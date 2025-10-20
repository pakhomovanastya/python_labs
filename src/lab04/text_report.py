import sys
sys.path.append(r'C:\Users\First\Documents\GitHub\python_labs\src\lib')
# импортирует модуль sys, который предоставляет доступ к объектам и функциям
from text_3 import *
from io_txt_csv import read_text, write_csv
from analyze_text import analyze_text

input_text = read_text(r'C:\Users\First\Documents\GitHub\python_labs\src\data\input_2.txt')
# читаем текст из указанного файла
analyze_text(input_text)

write_csv(top_n(tokenize(normalize(input_text)), 20), path=r'C:\Users\First\Documents\GitHub\python_labs\src\data\check_2.csv', header= ['WORD', 'COUNT'])
# нормализуем текст, разбиваем на слова, получаем топ-... слов
# write_csv(...) - записываем в CSV файл с заголовком ['WORD', 'COUNT'] и сохраняет файл
