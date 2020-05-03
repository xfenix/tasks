"""This is part1 of infinite tasks pile.
"""
import random
import typing

import pytest

from . import base


class FindSubstringInStringTask(base.BasicTask):
    """Task #6.

    Level: easy
    Description: given string, need to find it in other string, otherwise return -1
    """

    def task(self, haystack: str, needle: str) -> int:
        """Task body
        """
        if haystack == needle or not needle:
            return 0
        if not haystack or len(haystack) < len(needle):
            return -1
        for index, one_char in enumerate(haystack):
            if one_char == needle[0] and len(needle) <= len(haystack) - index + 1 and\
                haystack[index:index + len(needle)] == needle:
                return index
        return -1

    @pytest.mark.parametrize(
        "one_case",
        (
            dict(haystack="missisipi", needle="isip", result=4),
            dict(haystack="missisipi", needle="pi", result=7),
            dict(haystack="hellol", needle="ll", result=2),
            dict(haystack="", needle="", result=0),
            dict(haystack="", needle="i", result=-1),
            dict(haystack="help", needle="a", result=-1),
        ),
    )
    def test_basic(self, one_case):
        """Basic test.
        """
        fn_result: int = self.task(one_case["haystack"], one_case["needle"])
        assert fn_result == one_case["result"],\
               f'Given: {one_case["haystack"]}, {one_case["needle"]}, Returned: {fn_result}'
