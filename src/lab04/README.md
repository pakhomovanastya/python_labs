Лабораторная работа №4
=
Задание 1
> Реализуйте функции:
> > read_text(path: str | Path, encoding: str = "utf-8") -> str \
> > Открыть файл на чтение в указанной кодировке и вернуть содержимое как одну строку.\
> > Обрабатывать ошибки: если файл не найден — поднимать FileNotFoundError (пусть падает), если кодировка не подходит — поднимать UnicodeDecodeError (пусть падает).\
> > НО: в докстринге опишите, как пользователь может выбрать другую кодировку (пример: encoding="cp1251").\

> Объявление функции:
> > path - может быть строкой или объектом Path (путь к файлу)
> > encoding - кодировка файла, по умолчанию "utf-8"
>  p = Path(path)
> > Создание объекта Path: Преобразуем входной путь в стандартный объект Path для удобной работы.
> Чтение файла:
> > try: - начинаем блок где может возникнуть ошибка
> > p.read_text(encoding=encoding) - читаем ВЕСЬ файл как одну строку в указанной кодировке
> Обработка ошибки "Файл не найден":
> > Если файла нет - печатаем сообщение и возвращаем None
> Обработка ошибки кодировки:
> > Если файл в другой кодировке (не UTF-8) - печатаем сообщение и возвращаем None
### ![Изображение](https://github.com/user-attachments/assets/90b1cf75-1274-429d-b6d6-354813e53d89)
>
> > tokenize(text: str) -> list[str] \
### ![Изображение](https://github.com/user-attachments/assets/2e1ec975-d6b7-4baa-bfb2-dc4d5bdd6123)
>
> >count_freq(tokens: list[str]) -> dict[str, int]\
### ![Изображение](https://github.com/user-attachments/assets/857d2f75-57e0-4917-9226-b1c6aa34f7d8)
>
> >top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]
### ![Изображение](https://github.com/user-attachments/assets/85df6714-143c-44b5-b47a-31fb6a19e46f)
>
> >Вывод
### ![Изображение](https://github.com/user-attachments/assets/c4ee5145-8087-4117-a91f-2aa4161391ec)
>  Вывод 1
### ![Изображение](https://github.com/user-attachments/assets/f0c7c645-da8b-4cd8-9b3f-26e0eb658127)
>  
>  Вывод 2
### ![Изображение](https://github.com/user-attachments/assets/99c99009-060c-4267-b93c-2aa09655a92f)
> 
>  Вывод 3
### ![Изображение](https://github.com/user-attachments/assets/65d64c7d-67aa-47c4-ba39-577b49ea6219)

Задание 2

### ![Изображение](https://github.com/user-attachments/assets/e6ef7b21-4a48-439c-899b-d432db0394d0)
>
> > Вывод
> ### ![Изображение](https://github.com/user-attachments/assets/71dfcd98-419b-4c3d-88f0-b6f24b91845a)


