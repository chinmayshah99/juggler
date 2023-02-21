from pyjuggler import juggler
from typing import List


def square(x):
    return x * x


def square_delayed(x):
    import time

    time.sleep(1)
    return x * x


def test_square():
    len_input = 10
    input = [(2,) for _ in range(len_input)]
    response: List = juggler.run_process(square, input)
    assert len(response) == len_input
    assert response[0] == 4


def test_square_delayed():
    len_input = 10
    input = [(2,) for _ in range(len_input)]
    response: List = juggler.run_process(square_delayed, input)
    assert len(response) == len_input
    assert response[0] == 4
