from collections import deque

class Stack:
    """Реализация стека (LIFO) на базе списка"""
    def __init__(self):
        """Инициализирует пустой стек"""
        # внутреннее хранилище стека
        self._data = []

    def push(self, item):
        """Добавляет элемент на вершину стека"""
        # корректно: добавление в конец списка O(1) амортизированно
        #item элемент для добавления
        self._data.append(item)

    def pop(self):
        """Удаляет и возвращает элемент с вершины стека"""
        if self._data == []:
            raise IndexError("Стек пуст! Нельзя делать pop() из пустого стека")
        return self._data.pop()

    def peek(self):
        """Возвращает элемент с вершины стека без удаления"""
        if self._data == []:
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        """Проверяет пуст ли стек"""
        return len(self._data) == 0
    
    def __len__(self):
        """Возвращает количество элементов в стеке"""
        return len(self._data)


class Queue:
    """Реализация очереди (FIFO) на базе deque"""
    def __init__(self):
        """Инициализирует пустую очередь"""
        # ошибка: вместо deque используется list → операции O(n)
        self._data = deque()

    def enqueue(self, item):
        """Добавляет элемент в конец очереди"""
        # ошибка: вставка в начало, а не в конец
        self._data.append(item)

    def dequeue(self):
        """Удаляет и возвращает элемент из начала очереди"""
        # ошибка: удаление с конца, а не с начала
        #Если очередь пустая — исключение (например, IndexError)
        if len(self._data) == 0:
            raise IndexError("Очередь пустая! нельзя делать dequeue() из усткой очереди.")
        return self._data.popleft()

    def peek(self):
        """Возвращает первый элемент очереди без удаления"""
        # TODO: корректное поведение при пустой очереди
        if len(self._data) == 0: #Первый элемент очереди или None, если очередь пуста
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        """Проверяет, пуста ли очередь"""
        return len(self._data) == 0
    
    def __len__(self):
        """Возвращает количество элементов в очереди"""
        return len(self._data)