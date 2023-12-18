"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from src.stack import Stack

point = Stack()


def test_push():
    point.push(2)
    assert point.top.data == 2
    assert str(point) == '2'

def test_pop():
    point1 = Stack()
    point1.push(2)
    assert point1.pop() == 2

def test_str():
    point.push(2)
    assert str(point) == '22'
