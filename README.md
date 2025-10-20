[Лабораторная работа №1](src/lab01) 
Фотографии к [лабораторной работе №1](images/lab01)
= 
>
>
[Лабораторная работа №2](src/lab02)
Фотографии к [лабораторной работе №2](images/lab02)
=
>
Задание 1
> Реализуйте функции:
> > min_max(nums: list[float | int]) -> tuple[float | int, float | int] \
> > Находим длину цифр, всего в списке должно быть 2 цифры: max, min.\
> > Ф. raise выводит ошибку, если список пуст.
>
> > unique_sorted(nums: list[float | int]) -> list[float | int] \
> > sorted - сортирует список по возрастанию, set сохраняет различные цифры без повторений.
>
> >flatten(mat: list[list | tuple]) -> list\
> >«Расплющить» список списков => нам нужно из списка в спике объединить в единый спиок.
> >Создаём список куда будем добавлять значения с типом list/tuple с помощью ф. isinstance.\
> >Если значения не являются списком/кортежем ф.riase выводит ошибку TypeError.
>
### ![Изображение](https://github.com/user-attachments/assets/8d84cbba-de49-4a1b-8e4a-abed6cc7c971)
>
> > Вывод 1
> ### ![Изображение](https://github.com/user-attachments/assets/b0777166-662d-428c-a1b0-cd341bec262f)
>  
> > Вывод 2
> ### ![Изображение](https://github.com/user-attachments/assets/50d31fa3-5eea-4c49-bf3a-1cb2e04c0d9d)
> 
> > Вывод 3
> ### ![Изображение](https://github.com/user-attachments/assets/4de20e12-43c8-476d-b048-84eec29e0c2b)

>

Задание 2
> Реализуйте функции:
> > transpose(mat: list[list[float | int]]) -> list[list]
> > Поменять строки и столбцы местами, для этого строки должны быть одной длины.
> > Иначе ф.raise выводит ошибку ValueError
> 
> >row_sums(mat: list[list[float | int]]) -> list[float]
> >Сумма по каждой строке, перебираем числа, проверяем что ненулевой список и\
> >можем считать числа в этом списке.
> >Требуется прямоугольность => строки == столбцам.
> >Если длина = 0, то возвращяем пустой список.
> 
> >col_sums(mat: list[list[float | int]]) -> list[float]
> >Сумма по каждому столбцу => опять перебор чисел в ненулевом списке,\
> >ипсользуем ф.transpose, чтоб поменять строки и столбцы местами\
> >и уже только тогда считаем сумму.
> >Иначе ф.raise выводит ошибку ValueError, что строки разной длины.
>
### ![Изображение](https://github.com/user-attachments/assets/a03475f6-c6c5-4ed7-aa63-dd0ccb9eb402)
>
> >Вывод 1
>### ![Изображение](https://github.com/user-attachments/assets/826dc58a-4eac-4ca8-a948-16fa77de2c0b)
>
> >Вывод 2
>### ![Изображение](https://github.com/user-attachments/assets/7791adc4-3fad-4bf8-a872-f9cedd3776a0)
>
> >Вывод 3
>### ![Изображение](https://github.com/user-attachments/assets/f9ae4dc7-cd30-4558-a227-1e7c2d254b1f)
>

Задание 3
> Реализуйте функции:
> > format_name(name: str) -> str
> >Первое мы проверим, что есть ФИО, т.е. длина списка равна 3.
> > Так как это список мы переприсваевыем переменные.\
> > last_name это фамилия, где понадобить полное слово.
> > first_name это имя от которого нам нужен первый символ.
> > middle_name это отчество, где нам нужен первый символ.
> > Ф. f-string помогает вывести ФИО с нужными нам точками/запятыми
> > Так же мы делаем с ФИ, но если нет фамилии, то ф.raise выводит ошибку ValueError
> 
> >format_group(group: str) -> str
> >Здесь нам нужна группа, Ф. f-string помогает нам это осуществить.\
> >f"гр. {group}" => на выводе мы уже увидим не просто BIVT-25, но уже с добавлением гр.
> 
> >def format_gpa(gpa: float) -> str
> >Ф.isinstance(gpa, float) нам нужен тип float, как раз она это и проверяет,\
> >т.к. нужны значения после запятой(дробные,десятичные числа).
> >Если неверный тип GPA, тогда ф.raise выводит ошибку.
>
> >format_record(rec: tuple[str, str, float]) -> str
> >Финальная ф., в которой мы переприсваеваем три функции и можем использовать одновременно.
>
### ![Изображение](https://github.com/user-attachments/assets/8747edf6-ac53-4557-999c-f3f0560bf02f)
>
> >Вывод 
>### ![Изображение](https://github.com/user-attachments/assets/c11923f6-a933-414b-be0a-f0b65918e39c)

Лабораторная работа №3
=
Задание 1
> Реализуйте функции:
> > normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str \
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

>  cd путь к файлу
> 1) cd путь к файлу
> 2) $OutputEncoding = [System.Text.Encoding]::UTF8
> 3) echo "Привет, мир! Привет!!!" | py text_stats.py
