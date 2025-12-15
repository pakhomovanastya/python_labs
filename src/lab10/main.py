from structures import Stack, Queue
from linked_list import SinglyLinkedList

def main():
    
    print("Stack cheak")
    my_stack = Stack()
    # # my_stack.pop() #выведит ошибку
    print(f"Стек пуст: {my_stack.is_empty()}") #должен вернуть True
    print(f"Длина стека: {len(my_stack)}")
    my_stack.push(1)
    my_stack.push(3)
    my_stack.push(5)
    my_stack.push(7)
    print(f"Длина стека: {len(my_stack)}")
    print(f"Вершина: {my_stack.peek()}")
    while not my_stack.is_empty():  #пока не пусткой выведи последний и покажи и тд, 
                                    #когда стек станет пустым мы выйдим из этого списка
        # print(my_stack.peek()) #выведен 7, в стеке остунуться 1, 3, 5
        print(my_stack.pop()) #выводит в обратном порядке


    print('Queue cheak')
    my_queue = Queue()
    print(f"Очередь пуста: {my_queue.is_empty()}") #должен вернуть True
    print(f"Длина очереди: {len(my_queue)}")
    my_queue.enqueue(1)
    my_queue.enqueue(3)
    my_queue.enqueue(5)
    my_queue.enqueue(7)
    print(f"Первый элемент: {my_queue.peek()}") #посмотреть первый элемент, не удаляя
    print(f"Длина оочереди: {len(my_queue)}")
    while not my_queue.is_empty():
        print(f"Dequeue: {my_queue.dequeue()}") #выводит в прямом порядке


    print('SLList chek')
    my_list = SinglyLinkedList()
    my_list.append(1)
    my_list.append(3)
    my_list.append(5)
    my_list.append(7)
    my_list.prepend(0)
    print(f"Список: {my_list}")
    my_list.insert(1, 10)
    my_list.insert(0, -1)
    my_list.insert(7, 100)
    print(my_list)



if __name__ == '__main__':
    main()
    