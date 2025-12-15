Лабораторная работа №10
=
lab10/structures.py
---
```python
class Stack:
    def __init__(self):
        # _data - это обычный список Python, где будем хранить элементы
        # _ перед именем означает "внутренняя" переменная, 
        # пользователь не должен к ней обращаться напрямую
        self._data = []

    def push(self, item):
        # Добавляем элемент в конец списка
        # В Python append работает быстро (O(1) в среднем)
        self._data.append(item)
        # Пример: было [1, 2], push(3) → [1, 2, 3]
        # Вершина стека всегда последний элемент списка

    def pop(self):
        # Проверяем, не пуст ли стек
        if self._data == []:
            # Если пуст, выбрасываем ошибку
            raise IndexError("Стек пуст! Нельзя делать pop() из пустого стека")
        
        # Удаляем и возвращаем последний элемент
        return self._data.pop()
        # Пример: было [1, 2, 3], pop() → возвращает 3, остается [1, 2]

    def peek(self):
        # Смотрим на верхний элемент, но не удаляем его
        if self._data == []:
            return None  # Если стек пуст, возвращаем None
        return self._data[-1]  # [-1] - последний элемент списка

    def is_empty(self):
        # Проверяем, пуст ли стек
        return len(self._data) == 0
        # True - если пуст, False - если есть элементы

    def __len__(self):
        # Магический метод, вызывается при использовании len(stack)
        return len(self._data)

stack = Stack()      # Создаем пустой стек: []
stack.push(1)        # Добавляем 1: [1]
stack.push(2)        # Добавляем 2: [1, 2]
stack.peek()         # Смотрим верхний элемент: 2 (стек: [1, 2])
stack.pop()          # Удаляем верхний: возвращает 2, стек: [1]
stack.pop()          # Удаляем верхний: возвращает 1, стек: []
stack.is_empty()     # Проверяем: True
```

Очередь (Queue)
---
>Новый человек встает в конец очереди (enqueue)
>
>Обслуживают человека в начале очереди (dequeue)
>
>Первый пришедший обслуживается первым (FIFO)
```python
from collections import deque  # Импортируем специальную структуру

class Queue:
    def __init__(self):
        # Используем deque (двусвязную очередь) вместо обычного списка
        # Почему? Потому что удаление из начала списка медленное (O(n)),
        # а deque позволяет удалять из начала быстро (O(1))
        self._data = deque()

    def enqueue(self, item):
        # Добавляем элемент в КОНЕЦ очереди
        self._data.append(item)
        # Пример: было [1, 2], enqueue(3) → [1, 2, 3]
        # (в deque это выглядит так: deque([1, 2, 3]))

    def dequeue(self):
        # Проверяем, не пуста ли очередь
        if len(self._data) == 0:
            raise IndexError("Очередь пустая!")
        
        # Удаляем и возвращаем элемент из НАЧАЛА
        return self._data.popleft()
        # popleft() - специальный метод deque для удаления слева
        # Пример: было [1, 2, 3], dequeue() → возвращает 1, остается [2, 3]

    def peek(self):
        # Смотрим на первый элемент, но не удаляем
        if len(self._data) == 0:
            return None
        return self._data[0]  # [0] - первый элемент

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

queue = Queue()      # Создаем пустую очередь: []
queue.enqueue(1)     # Добавляем 1: [1]
queue.enqueue(2)     # Добавляем 2: [1, 2]
queue.peek()         # Смотрим первый: 1 (очередь: [1, 2])
queue.dequeue()      # Удаляем первый: возвращает 1, очередь: [2]
queue.dequeue()      # Удаляем первый: возвращает 2, очередь: []
queue.is_empty()     # Проверяем: True
```
lab10/linked_list.py Односвязный список
---
Узел (Node)
```python
class Node:
    def __init__(self, value, next=None):
        self.value = value  # Значение, которое хранит узел (например, число 5)
        self.next = next    # Ссылка на следующий узел
        
        # next может быть:
        # - None (если это последний узел)
        # - другим Node (если есть следующий узел)
```
Сам список (SinglyLinkedList)
---
```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Голова списка - первый узел или None если пусто
        self._size = 0    # Счетчик элементов
```

1. Добавление в конец (append)
```python
def append(self, value):
    # Создаем новый узел
    new_node = Node(value)
    
    # Если список пуст, новый узел становится головой
    if self.head is None:
        self.head = new_node
        self._size += 1
        return
    
    # Если список не пуст, идем до последнего узла
    current = self.head  # Начинаем с головы
    while current.next is not None:  # Пока есть следующий узел
        current = current.next      # Переходим к нему
    
    # Теперь current - последний узел
    # Присоединяем новый узел к нему
    current.next = new_node
    self._size += 1
```
Пустой список: head = None
>append(1): head → [1|None]
>append(3): head → [1|•] → [3|None]
>append(5): head → [1|•] → [3|•] → [5|None]

2. Добавление в начало (prepend)
```python
def prepend(self, value):
    # Создаем узел, который ссылается на текущую голову
    new_node = Node(value, next=self.head)
    
    # Новый узел становится новой головой
    self.head = new_node
    self._size += 1
```
>До:      head → [1|•] → [3|•] → [5|None]
>После:   head → [0|•] → [1|•] → [3|•] → [5|None]

3. Вставка по индексу (insert)
```python
def insert(self, idx, value):
    # Проверяем корректность индекса
    if idx < 0:
        raise IndexError("Negative index is not supported")
    if idx > self._size:
        raise IndexError("Index is too large")
    
    # Если вставляем в начало, используем prepend
    if idx == 0:
        self.prepend(value)
        return
    
    # Ищем узел ПЕРЕД позицией вставки
    current = self.head
    for _ in range(idx - 1):  # Идем idx-1 шагов
        current = current.next
    
    # Вставляем новый узел
    new_node = Node(value, next=current.next)
    current.next = new_node
    self._size += 1
```
 
4. Удаление по индексу (remove_at)
---
```python
def remove_at(self, idx):
    # Проверка индекса
    if idx < 0 or idx >= self._size:
        raise IndexError(f"Index {idx} out of range")
    
    # Удаление из начала
    if idx == 0:
        value = self.head.value
        self.head = self.head.next  # Голова теперь следующий узел
        self._size -= 1
        return value
    
    # Удаление из середины или конца
    current = self.head
    # Ищем узел ПЕРЕД удаляемым
    for _ in range(idx - 1):
        current = current.next
    
    # Запоминаем значение удаляемого узла
    value = current.next.value
    # Пропускаем удаляемый узел
    current.next = current.next.next
    self._size -= 1
    
    return value
```

5. Итератор (iter)
```python
def __iter__(self):
    current = self.head
    while current is not None:
        yield current.value  # Возвращаем значение текущего узла
        current = current.next  # Переходим к следующему
    
# yield делает функцию генератором
# Это позволяет писать for value in my_list
```
lab10/structures.py
<img width="1242" height="851" alt="structures py" src="https://github.com/user-attachments/assets/48ec7fee-c7b5-4737-a16d-977c08d0476c" />
<img width="1142" height="861" alt="structures py 2 часть" src="https://github.com/user-attachments/assets/8c9e671a-20cf-4341-a1a6-05f6c9ba48e7" />

lab10/linked_list.py
<img width="1255" height="1011" alt="linked_list py" src="https://github.com/user-attachments/assets/5fe7de3d-06c5-4ab2-ba59-0a7213bd308a" />
<img width="1255" height="1011" alt="linked_list py" src="https://github.com/user-attachments/assets/0ebdaca7-150d-4096-afd5-13fa241993bf" />
<img width="795" height="435" alt="linked_list py 3 часть" src="https://github.com/user-attachments/assets/22b5c8ff-31ff-4f74-9ee1-a6d5d493f016" />

lab10/main.py
<img width="1021" height="860" alt="main 1 часть" src="https://github.com/user-attachments/assets/82169df2-41c0-4abe-88bb-3e2d70e1d75e" />
<img width="1077" height="475" alt="main 2 часть" src="https://github.com/user-attachments/assets/5e52b36f-108a-4b3c-afc0-a73b2239e38a" />

вывод
<img width="866" height="521" alt="вывод" src="https://github.com/user-attachments/assets/1137c960-8c86-48f5-90d5-5d1648e55258" />
