"""Tasks helpers.
"""
from __future__ import annotations
import abc
import typing
import dataclasses


class BasicTask(abc.ABC):
    """Basic task class.
    """

    fixtures: typing.List[typing.Dict[str, typing.Any]] = [
        dict(input=None, result=None),
    ]

    def task(self, input_data: typing.Any) -> typing.Any:
        """Body for task
        """
        raise NotImplementedError()

    def test_basic(self):
        """Basic test.
        """
        for one_test in self.fixtures:
            fn_result: typing.Any = self.task(one_test["input"])
            assert fn_result == one_test["result"], f'Expected: {one_test["result"]}, Returned: {fn_result}'


@dataclasses.dataclass
class LinkedListNode:
    """Linked list basic node
    """

    value: typing.Any
    next: LinkedListNode = None


def build_linked_list(list_of_values: typing.List[typing.Any]) -> LinkedListNode:
    """Helper for building linked lists
    """
    inner_list: typing.List = list_of_values[:]
    head_of_list: LinkedListNode = LinkedListNode(inner_list.pop(0))
    current_pointer: LinkedListNode = head_of_list
    for one_item in inner_list:
        current_pointer.next = LinkedListNode(one_item)
        current_pointer = current_pointer.next
    return head_of_list
