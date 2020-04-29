"""Tasks helpers
"""
import abc
import typing


class BasicTask(abc.ABC):
    """Basic task class
    """

    fixtures: typing.List[typing.Dict[str, typing.Any]] = [
        dict(input=None, result=None),
    ]

    def task(self, input_data: typing.Any) -> typing.Any:
        """Body for task
        """
        raise NotImplemented()

    def test_basic(self):
        """Basic test
        """
        for one_test in self.fixtures:
            fn_result: typing.Any = self.task(one_test['input'])
            assert fn_result == one_test['result'], f'Expected: {one_test["result"]}, Returned: {fn_result}'


def test_task_error():
    BasicTask().task()
