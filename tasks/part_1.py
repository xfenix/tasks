"""This is part1 of infinite tasks pile
"""
import typing


class SortOddNumbersTask:
    """Task #1

    Level: easy
    Description: sort array of numbers, where only odd numbers must be sorted
    """

    fixtures: typing.Dict = dict(
        input=[8, 10, 1, 15, 66, -20, 30],
        result=[],
    )

    def sort_odd(self, input_array: typing.List) -> typing.List:
        """
        """

    def test_sort(self):
        """
        """
        assert self.sort_odd(self.fixtures['input']) == self.fixtures['result']
