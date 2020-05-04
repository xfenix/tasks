"""This is part1 of infinite tasks pile.
"""
import random
import typing

import pytest

from . import base


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


class FindUniqueInDuplicatesTask(base.BasicTask):
    """Task #7.

    Level: easy
    Description: given array of duplcates, where 1 number is uniqe Need to find it
    Constraints:
        Time complexity O(n)
        Space complexity O(1)
        No array modifications
    """

    fixtures: typing.List[typing.Dict[str, typing.Union[typing.List[int], int]]] = [
        dict(input=[500, 200, 100, 100, 200, 300, 300], result=500),
        dict(input=[1, 2, 3, 3, 2, 1, 5], result=5),
    ]

    def task(self, input_array: typing.List[int]) -> typing.Set:
        """Task body.
        """
        unique: int = 0
        for one_item in input_array:
            unique ^= one_item
        return unique
