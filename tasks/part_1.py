"""This is part1 of infinite tasks pile
"""
import typing

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
