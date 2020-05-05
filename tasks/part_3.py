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

    def task(self, haystack: str, needle: str) -> int:
        """Task body
        """
        pass

    @pytest.mark.parametrize(
        "one_case", (dict(input=dict(list=base.build_linked_list([1, 2, 3, 4, 5, 6]), nth=2), result=5),),
    )
    def test_basic(self, one_case):
        """Basic test.
        """
        pass
