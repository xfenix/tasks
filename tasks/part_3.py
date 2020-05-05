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

    def task(self, linked_list: str, nth: str) -> typing.Optional[int]:
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
        ),
    )
    def test_basic(
        self, one_case: typing.Dict[str, typing.Union[int, typing.Dict[str, typing.Union[int, base.LinkedListNode]]]]
    ) -> None:
        """Basic test.
        """
        assert self.task(one_case["input"]["list"], one_case["input"]["nth"]) == one_case["result"]
