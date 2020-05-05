"""Basic tests for some infra things.
"""
import sys
import types
import random
import importlib
from unittest import mock

import pytest

from tasks import base


@pytest.mark.parametrize("action_value", ["_no_action_lol", "list"])
def test_main_cli(monkeypatch, action_value):
    """Funny __main__.py test.
    We have some difficulties in testing: correctly mock argparse, and reload module. But now its ok
    """
    module_path: str = "tasks.__main__"
    need_reload: bool = module_path in sys.modules
    fake_parser_inner: mock.Mock = mock.Mock(parse_args=mock.Mock(return_value=mock.Mock(action=action_value)))
    monkeypatch.setattr("argparse.ArgumentParser", mock.Mock(return_value=fake_parser_inner))
    monkeypatch.setattr("builtins.print", mock.Mock())
    module: types.ModuleType = importlib.import_module(module_path)
    if need_reload:
        importlib.reload(module)


def test_base_task():
    """Test for BasicTask.
    """
    new_class: base.BasicTask = base.BasicTask()
    with pytest.raises(NotImplementedError):
        new_class.task(random.randrange(10 ** 2, 10 ** 4))


@pytest.mark.parametrize("one_case", ((1, 2, 3), (10, 20, 30), range(1, 201)))
def test_linked_list_creator(one_case):
    """Test for linked list creator.
    """
    one_case: typing.List = list(one_case)
    cursor: int = 0
    linked_list: base.LinkedListNode = base.iter_to_linked(one_case)
    while linked_list != None:
        assert linked_list.value == one_case[cursor]
        linked_list = linked_list.next
        cursor += 1
