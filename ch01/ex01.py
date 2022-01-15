#!/usr/bin/env python3
# ex1.py
# Reference: http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html 

import math
import random
import time
import unittest

from typing import List

from fib5 import fib5

def fib5(n: int) -> int:
    if n == 0: return n  # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
    return next

def fib7(n: int) -> int:
    phi: float = (1 + math.sqrt(5)) / 2
    return round(pow(phi, n) / math.sqrt(5))


class TestMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.range = 30
        self.iteration = 10

    def test_value(self) -> None:
        for _ in range(self.iteration):
            n: int = random.randint(0, self.range)
            self.assertEqual(fib7(n), fib5(n))

    def test_execution_time(self) -> None:
        samples: List[int] = [random.randint(0, self.range) for _ in range(self.iteration)]
        fib5_time: float = time.time()
        fib5s = [fib5(n) for n in samples]
        fib5_time = time.time() - fib5_time

        fib7_time: float = time.time()
        fib7s = [fib7(n) for n in samples]
        fib7_time = time.time() - fib7_time

        self.assertLessEqual(fib7_time, 2 * fib5_time)


if __name__ == "__main__":
    unittest.main()
