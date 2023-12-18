class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data= data
        self.next_node = next_node


class Stack:
    """Класс для стека"""
    all = ''

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def __str__(self):
        return self.all

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node
        if self.all == '':
            self.all += f'{self.top.data}'
        else:
            self.all += f'\n{self.top.data}'

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.all = self.all[:len(self.all) - (len(str(self.top.data))+1)]
            self.top = self.top.next_node
            return popped_node.data
