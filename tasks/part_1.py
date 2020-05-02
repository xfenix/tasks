"""This is part1 of infinite tasks pile
"""
import random
import typing

import pytest

from . import base


class SortOddNumbersTask(base.BasicTask):
    """Task #1

    Level: easy
    Description: sort array of numbers, where only odd numbers must be sorted
    Must be in place
    """

    fixtures: typing.List[typing.Dict[str, typing.List[int]]] = [
        dict(input=[2, 3, 7, 4, 6, 1, 5, 8, 9], result=[2, 1, 3, 4, 6, 5, 7, 8, 9],),
        dict(input=[20, 33, 44, 1, 4, -55], result=[20, -55, 44, 1, 4, 33],),
    ]

    def task(self, input_array: typing.List[int]) -> typing.List[int]:
        """Task body
        """
        even_array: typing.Iterator[int] = sorted(
            [one_item for one_item in input_array if one_item % 2]
        )
        for index, one_item in enumerate(input_array):
            input_array[index] = even_array.pop(0) if one_item % 2 else one_item
        return input_array


class CompatStringTask(base.BasicTask):
    """Task #2

    Level: easy
    Description: compat string
    """

    fixtures: typing.List[typing.Dict[str, str]] = [
        dict(input="AAAAABBBBCCCCCDEEE", result="A5B4C5DE3",),
    ]

    def task(self, input_str: str) -> str:
        """Task body
        """
        output_str: typing.List = []
        store_fn: typing.Callable = lambda char, counter: output_str.append(
            f'{char}{counter if counter > 1 else ""}'
        )
        current_char: str = ""
        current_counter: int
        for one_char in input_str:
            if one_char != current_char:
                if current_char:
                    store_fn(current_char, current_counter)
                current_char = one_char
                current_counter = 1
            else:
                current_counter += 1
        store_fn(current_char, current_counter)
        return "".join(output_str)


class CalculatePIFromRandomTask(base.BasicTask):
    """Task #3

    You get N random points from 0 to 1 with uniform distribution,
    you need to calculate PI number from this (approximately)
    """

    def task(self, points: int) -> float:
        """This solution may be very hard to understand.
        Look, you have points from 0 to 1. So, if you use them in 2D dimension,
        you can get (X, Y) pair. This pair - dot in square with side 1.
        Next you need to draw square with side 2, with 0, 0 point in the middle.
        To find PI you need to draw circle in those point and place in in the square.
        Now back to our dimension, from 0 to 1 in X axis and from 0 to 1 in Y axis.
        Now we have 1/4 of cirle in 1/4 of square. To find PI in this, you need to divide
        circle area to square area (all two divided by 4). Those ratio similar to numbers of dots
        in 1/4 of circle divided by all dots (because of uniform distribution).
        So, formula will be like this:

        (PI * r**2)/4 / 4/4  =  points_in_circle/points
            and, simplify
        PI = 4 * (points_in_circle/points)

        Now we must calculare points_in_circle, to do so we need to draw triangle.
        If hypotenuse will be 1 or less - then point in circle. Formula of this is:
    
        hypotenuse = sqrt(random_x ** 2 + random_y ** 2)

        But we talking about radius of size 1, so square root of 1 is one, less then 1 - less then 1, else more.
        In other words, we can skip square root calculation. So, now, job is done
        """
        points_in: int = 0
        for _ in range(points):
            if random.random() ** 2 + random.random() ** 2 < 1:
                points_in += 1
        return 4 * points_in/points

    @pytest.mark.parametrize('one_case', (
        dict(input=100, result_from=2.7, result_to=3.5),
        dict(input=1000, result_from=3.0, result_to=3.3),
        dict(input=100000, result_from=3.12, result_to=3.16),
    ))
    def test_basic(self, one_case):
        """Override basic test
        """
        result: float = self.task(one_case['input'])
        print(f'Testing PI generator for {one_case["input"]} times, result: {result}')
        assert one_case['result_from'] < result < one_case['result_to']
