Лабораторная работа №2
=
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
