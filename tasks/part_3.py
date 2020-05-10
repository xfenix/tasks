"""
"""
import typing

import pytest

from tasks import base


class GetNthFromLinkedListEndTask(base.BasicTask):
    """Task #10.

    Level: easy
    Description: given linked list, return nth-element from the end
    Example: list: 1 -> 2 -> 20 -> 4 -> 5, n: 3, returns: 20
    """

    def task(self, linked_list: str, nth: int) -> typing.Optional[int]:
        """Task body
        """
        first_pointer: base.LinkedList = linked_list
        second_pointer: base.LinkedList = linked_list
        for _ in range(nth):
            if not first_pointer:
                return None
            first_pointer = first_pointer.next
        while first_pointer != None:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next
        return second_pointer.value

    @pytest.mark.parametrize(
        "one_case",
        (
            dict(input=dict(list=base.iter_to_linked([1, 2, 3, 4, 5, 6]), nth=2), result=5),
            dict(input=dict(list=base.iter_to_linked([10, 30, 40]), nth=1), result=40),
            dict(input=dict(list=base.iter_to_linked([]), nth=122), result=None),
        ),
    )
    def test_basic(
        self,
        one_case: typing.Dict[str, typing.Union[int, None, typing.Dict[str, typing.Union[int, base.LinkedListNode]]]],
    ) -> None:
        """Basic test.
        """
        assert self.task(one_case["input"]["list"], one_case["input"]["nth"]) == one_case["result"]


class AddOneTooArrayOfIntegersTask(base.BasicTask):
    """Task #11.

    Level: easy
    Description: given array of integers [1, 2, 3, 4], add 1 to last digit and return
                 array, as if input was regular integer and output like: [1, 2, 3, 5]
    """

    fixtures: typing.List[typing.Dict[str, typing.List[int]]] = [
        # dict(input=[5, 4, 3, 2], result=[5, 4, 3, 3],),
    ]

    def task(self, input_array: typing.List[int]) -> typing.List[int]:
        """Task body.
        TODO: wip
        """
        reverse_index: int = 0
        need_to_increase_next: bool = True
        for index in range(len(input_array)):
            reverse_index = len(input_array) - index
            if input_array[reverse_index] == 9:
                input_array[reverse_index] = 0
                need_to_increase_next = True
                continue
            if need_to_increase_next:
                input_array[reverse_index] += 1
                need_to_increase_next = False
                continue
            break
        return input_array


class OverlappingRectanglesTask(base.BasicTask):
    """Task #12.

    Level: easy
    Description: given two tuples with two pairs of X, Y coords, which represents
                 left bottom and right top cornes of rectangles. Need to find overlap square
    """

    fixtures: typing.List[
        typing.Dict[str, typing.Union[typing.Tuple[typing.Tuple[int]], typing.Union[bool, int]]]
    ] = [
        dict(input=((2, 1), (5, 5), (3, 2), (5, 7)), result=6,),
        dict(input=((1, 1), (3, 3), (10, 20), (50, 70)), result=False,),
        dict(input=((-10, -10), (-20, -20), (-5, -5), (-15, -15)), result=25,),
        dict(input=((-5, -1), (10, 10), (6, 6), (20, 31)), result=16,),
        dict(input=((-100, -1000), (-10, -10), (-15, -11), (100, 30)), result=5,),
    ]

    def task(self, input_struct: typing.Tuple[typing.Tuple[int]]) -> typing.Union[bool, int]:
        """Task body.
        TODO: wip
        """
        def search_2d_intersection(is_x: bool) -> int:
            """Helper function for intersection search by coord index
            """
            index: int = 0 if is_x else 1
            first_pair_max: int = max(input_struct[0][index], input_struct[1][index])
            second_pair_min: int = min(input_struct[2][index], input_struct[3][index])
            if first_pair_max > second_pair_min:
                return first_pair_max - second_pair_min
            else:
                return 0

        x_dist: int = search_2d_intersection(is_x=True)
        if not x_dist:
            return False
        y_dist: int = search_2d_intersection(is_x=False)
        if not y_dist:
            return False
        return x_dist * y_dist
