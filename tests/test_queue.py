"""Здесь надо написать тесты с использованием unittest для модуля queue."""
from src.queue import Queue
import pytest

queue = Queue()

def test_str():
    assert str(queue) == ''

def test_enqueue():
    queue.enqueue(2)
    assert str(queue) == '2'

def test_dequeue():
    queue.enqueue(3)
    queue.enqueue(2)
    assert str(queue) == '3\n2'
    queue.dequeue()
    assert str(queue) == '2'