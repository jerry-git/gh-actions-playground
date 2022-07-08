import random


def test_flaky1():
    if random.random() < 0.5:
        raise ValueError


def test_flaky2():
    if random.random() < 0.5:
        raise ValueError
