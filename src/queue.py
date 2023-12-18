class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""
    all = ''

    def __init__(self):
        """Конструктор класса Queue"""
        self.tail = None
        self.head = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            self.all += f'{node.data}'
        else:
            self.tail.next_node = node
            self.tail = node
            self.all += f'\n{node.data}'

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is None:
            return None
        else:
            popped_node = self.head
            self.all = self.all[(len(str(self.head.data)) + 1):]
            self.head = self.head.next_node
            return popped_node

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        return self.all
