"""This is part1 of infinite tasks pile.
"""
import random
import typing

import pytest

from . import base


class SortOddNumbersTask(base.BasicTask):
    """Task #1.

    Level: easy
    Description: sort array of numbers, where only odd numbers must be sorted
    Constraints: must be in place
    """

    fixtures: typing.List[typing.Dict[str, typing.List[int]]] = [
        dict(input=[2, 3, 7, 4, 6, 1, 5, 8, 9], result=[2, 1, 3, 4, 6, 5, 7, 8, 9],),
        dict(input=[20, 33, 44, 1, 4, -55], result=[20, -55, 44, 1, 4, 33],),
    ]

    def task(self, input_array: typing.List[int]) -> typing.List[int]:
        """Task body
        """
        even_array: typing.Iterator[int] = sorted([one_item for one_item in input_array if one_item % 2])
        for index, one_item in enumerate(input_array):
            input_array[index] = even_array.pop(0) if one_item % 2 else one_item
        return input_array


class CompatStringTask(base.BasicTask):
    """Task #2.

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
        store_fn: typing.Callable = lambda char, counter: output_str.append(f'{char}{counter if counter > 1 else ""}')
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
    """Task #3.

    Level: medium to hard?
    Description: You get N random points from 0 to 1 with uniform distribution,
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
        return 4 * points_in / points

    @pytest.mark.parametrize(
        "one_case",
        (
            dict(input=100, result_from=2.7, result_to=3.5),
            dict(input=1000, result_from=3.0, result_to=3.3),
            dict(input=100000, result_from=3.12, result_to=3.16),
        ),
    )
    def test_basic(self, one_case):
        """Override basic test.
        """
        result: float = self.task(one_case["input"])
        print(f'Testing PI generator for {one_case["input"]} times, result: {result}')
        assert one_case["result_from"] < result < one_case["result_to"]


class FindDuplicateTask(base.BasicTask):
    """Task #4.

    Level: medium?
    Description: given array n + 1 of numbers, where each item from 1 to n, find duplicate
    Constraints:
        Time complexity less then O(n^2)
        Space complexity O(1)
        Array must not be modified (e.g. read only)
    """

    fixtures: typing.List[typing.Dict[str, typing.Union[typing.List[int], int]]] = [
        dict(input=[1, 2, 3, 4, 5, 6, 7, 8, 7, 7], result=7),
        dict(input=[1, 2, 2, 2, 3, 4, 5], result=2),
        dict(input=[1, 2, 3, 4, 5, 4], result=4),
        dict(input=[3, 1, 3, 4, 2], result=3),
    ]

    def task(self, input_array: typing.List[int]) -> int:
        """This solution also very hard to understand.
        It's Ffloyd algorithm for cycle detection.
        It said that if we have list with cycle in it, then we can go through it with two
        pointers - usual (1 -> 2 -> 3...) and fast (usual x 2, 1 -> 3 ...). They call
        turtoise and hair. When they met, you must reset fast to beggining of the array, and left
        in meting point slow one. Then you need to start looping again while they met.
        And now, when they met, it is the start of the loop (in our case - dupliacte number)
        """
        turtoise: int = input_array[0]
        hair: int = input_array[0]
        while True:
            turtoise = input_array[turtoise]
            hair = input_array[input_array[hair]]
            if turtoise == hair:
                break
        hair: int = input_array[0]
        while hair != turtoise:
            hair = input_array[hair]
            turtoise = input_array[turtoise]
        return hair


class FindMissingMultipleTask(base.BasicTask):
    """Task #5.

    Level: easy
    Description: given array length n + 1 with 0 to n missed elements, need to find all of it
    """

    fixtures: typing.List[typing.Dict[str, typing.Set[int]]] = [
        dict(input=[1, 2, 3, 5, 6, 8, 10], result={4, 7, 9},),
        dict(input=[3, 4, 1, 9], result={2, 5, 6, 7, 8},),
    ]

    def task(self, input_array: typing.List[int]) -> typing.Set:
        """Task body.
        """
        min_element: int = min(input_array)  # O(n)
        max_element: int = max(input_array)  # O(n)
        return set(range(min_element, max_element + 1)) - set(input_array)  # O(n) + O(n)
