Лабораторная работа №4
=
Задание А
-
Пункт 1
> Реализуйте функции:
> > read_text(path: str | Path, encoding: str = "utf-8") -> str\
> > Открыть файл на чтение в указанной кодировке и вернуть содержимое как одну строку.\
> > Обрабатывать ошибки: если файл не найден — поднимать FileNotFoundError (пусть падает), если кодировка не подходит — поднимать UnicodeDecodeError (пусть падает).\
> > НО: в докстринге опишите, как пользователь может выбрать другую кодировку (пример: encoding="cp1251").\

> Объявление функции:
> > path - может быть строкой или объектом Path (путь к файлу)\
> > encoding - кодировка файла, по умолчанию "utf-8"\

>  p = Path(path)
> > Создание объекта Path: Преобразуем входной путь в стандартный объект Path для удобной работы.\

> Чтение файла:
> > try: - начинаем блок где может возникнуть ошибка\
> > p.read_text(encoding=encoding) - читаем ВЕСЬ файл как одну строку в указанной кодировке\

> Обработка ошибки "Файл не найден":
> > Если файла нет - печатаем сообщение и возвращаем None\

> Обработка ошибки кодировки:
> > Если файл в другой кодировке (не UTF-8) - печатаем сообщение и возвращаем None\
### ![Изображение](https://github.com/user-attachments/assets/a8a87d51-778e-440a-8f5e-ead3a93161dc)

Пункт 2
> Функция
> > write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None\
> > Создать/перезаписать CSV с разделителем ,.\
> > Если передан header, записать его первой строкой.\
> > Проверить, что каждая строка в rows имеет одинаковую длину (иначе ValueError).\

> Функция write_csv()
> >rows - итерируемый объект (можно перебирать) содержащий последовательности (строки, списки, кортежи)\
> >path - куда сохранить CSV файл\
> >header - заголовок таблицы, может быть None (без заголовка)\

> p = Path(path)
> rows = list(rows)\
> >Преобразуем rows в список (чтобы можно было несколько раз работать с данными)\

> with p.open("w", newline="", encoding="utf-8") as f:
> >with - контекстный менеджер (автоматически закроет файл)\
> >"w" - открываем для записи (перезапишет если файл существует)\
> >newline="" - специальная настройка для корректной работы с CSV\
> >encoding="utf-8" - записываем в кодировке UTF-8\

> w = csv.writer(f)
> >Создание CSV писателя: Объект который умеет записывать данные в CSV формате.\

> for r in rows:
> >Для каждой строки в rows проверяем что ее длина совпадает с длиной заголовка\
> >Если совпадает - записываем строку\
> >Если нет - вызываем ошибку ValueError\
### ![Изображение](https://github.com/user-attachments/assets/854c5f56-1655-433d-ba7e-23f3b6734807)

Пункт 3
>ensure_parent_dir(path: str | Path) -> None
> >Объявление функции: Принимает путь, ничего не возвращает.\

>parent_directory = os.path.dirname(path)
> >Получение родительской директории: os.path.dirname() возвращает путь к папке где лежит файл.\

>os.makedirs(parent_directory, exist_ok=True)
> > Создание директории: os.makedirs() - создает все папки в пути\
> >exist_ok=True - если папки уже существуют, не вызывает ошибку\
### ![Изображение](https://github.com/user-attachments/assets/ccf555c5-74ec-4c3a-85f7-6b400757a43f)

>Функция main() и запуск
> >if __name__ == '__main__': - код выполнится только если файл запущен напрямую
> >Читаем разные файлы, пробуем записать CSV
### ![Изображение](https://github.com/user-attachments/assets/b6daf944-3594-49c2-ab1c-e7f8f59a0ad7)


Вывод А
### ![Изображение](https://github.com/user-attachments/assets/c722895c-c218-493c-b332-a4faf6e49d80)

папка с check.csv
### ![Изображение](https://github.com/user-attachments/assets/ea2ed4ee-a2de-4c79-bd8e-1109f66337ae)

Задание B
-
Реализуйте функции: text_report.py
>Главный скрипт который все объединяет.
> >import sys\
> >sys.path.append(r'C:\Users\First\Documents\GitHub\python_labs\src\lib')\
> >from text_3 import *\

>Импорт функций текстовой обработки
> >from io_txt_csv import read_text, write_csv
> >from analyze_text import analyze_text

> Импорт наших модулей: Функции для ввода-вывода и анализа текста.
> >input_text = read_text(r'C:\Users\First\Documents\GitHub\python_labs\src\data\input_2.txt')

> Чтение входного файла: Читаем текст из указанного файла.
> >analyze_text(input_text)

> Анализ текста: Выводим статистику в консоль.
> >write_csv(top_n(tokenize(normalize(input_text)), 20), path=r'C:\Users\First\Documents\GitHub\python_labs\src\data\check_2.csv', header= ['WORD', 'COUNT'])
### ![Изображение](https://github.com/user-attachments/assets/ac505e25-5420-41a4-906e-195c4f535b87)

Вывод text_report_csv:
### ![Изображение](https://github.com/user-attachments/assets/7249425f-f2c9-4118-ba05-7266accd672b)

Файл input_2.txt
### ![Изображение](https://github.com/user-attachments/assets/a04ce99a-63c1-49a5-9866-9fe47873794c)

Файл check_2.csv
### ![Изображение](https://github.com/user-attachments/assets/8d416e8c-2795-42e4-83e3-4028bda0909b)








