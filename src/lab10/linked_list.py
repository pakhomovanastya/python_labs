class Node:
    """Узел односвязного списка"""
    def __init__(self, value, next=None):
        self.value = value #значение узла
        self.next = next   #ссылка на следующий узел или None


class SinglyLinkedList:
    """Односвязный список"""
    def __init__(self):
        """Инициализирует пустой список"""
        self.head = None #ссылка на первый узел или None
        self._size = 0   #количество элементов в списке

    def append(self, value):
        """Добавить элемент в конец списка"""
        new_node = Node(value) #value значение для добавления
        if self.head is None: #если список пуст, новый узел становится головой
            self.head = new_node
            self._size += 1
            return

        # неэффективность: полный обход списка O(n)
        current = self.head #текущий узел
        while current.next is not None: #пока след. эл. ссылающийся за текущим не является None, переходим на след
            current = current.next
        current.next = new_node
        self._size += 1

    def prepend(self, value):
        """Добавить элемент в начало списка"""
        new_node = Node(value, next=self.head) #создаем новый узел, который ссылается на текущую голову
        self.head = new_node #новый узел становится новой головой
        self._size += 1

    def insert(self, idx, value):
        """Вставка по индексу — неполная реализация, есть ошибки"""
        if idx < 0: #индекс для вставки (0 ≤ idx ≤ len(list))
            raise IndexError("Negative index is not supported")
        if idx > self._size:
            raise IndexError("Index is too. There are only {self._size} elements in the List")

        if idx == 0: #вставка в начало prepend
            self.prepend(value)
            return

        current = self.head #вставка в середину или конец
        for _ in range(idx - 1): #идем до узла, предшествующего позиции вставки
            current = current.next

        #создаем новый узел и вставляем его
        new_node = Node(value, next=current.next)
        current.next = new_node
        self._size += 1

    # Можно добавить для полноты:
    def remove_at(self, idx):
        """Удаляет элемент по указанному индексу"""
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size-1}]")
        
        if idx == 0:
            value = self.head.value
            self.head = self.head.next
            self._size -= 1
            return value
        
        current = self.head # Удаление из середины или конца
        for _ in range(idx - 1): # Ищем узел перед удаляемым
            current = current.next
        value = current.next.value #Запоминаем значение удаляемого узла
        current.next = current.next.next # Пропускаем удаляемый узел
        self._size -= 1
        return value

    def __iter__(self):
        """Возвращает итератор по значениям списка"""
        current = self.head
        while current is not None:
            yield current.value # Возвращаем значение текущего узла
                                # yield делает функцию генератором
            current = current.next  # Переходим к следующему

    def __len__(self):
        """Возвращает количество элементов в списке"""
        return self._size

    def __repr__(self):
        """Строковое представление списка"""
        values = list(self)
        return f"SinglyLinkedList({values})"