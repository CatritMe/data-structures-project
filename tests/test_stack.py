"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from src.stack import Node, Stack
import pytest


@pytest.fixture
def point():
    return Stack([1, 2, 3])


def test_push(point):
    Stack.push(point,2)
    assert point.top == [1, 2, 3, 2]

def test_pop():
    point1 = Stack()
    point1.push(2)
    assert point1.pop() == 2