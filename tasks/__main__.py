"""Simple CLI
"""
import types
import typing
import inspect
import argparse
import pathlib
import importlib


current_dir: pathlib.Path = pathlib.Path(__file__).parent.resolve()
parser_inst: argparse.ArgumentParser = argparse.ArgumentParser(description='CLI wrapper')
parser_inst.add_argument('action')
cli_arguments: argparse.Namespace = parser_inst.parse_args()

if cli_arguments.action == 'list':
    docs_map: typing.Dict = {}
    inner_key: str
    prepared_doc: str
    for one_mod_path in current_dir.glob('part_*.py'):
        if one_mod_path.is_file():
            one_module: types.ModuleType = importlib.import_module(f'.{one_mod_path.stem}', package='tasks')
            classes_list: typing.List = inspect.getmembers(one_module, inspect.isclass)
            for class_title, one_class_obj in classes_list:
                if class_title.endswith('Task'):
                    inner_key = one_class_obj.__doc__.split('\n')[0].rstrip('.').lstrip('Task #')
                    prepared_doc = one_class_obj.__doc__.replace(' ' * 4, '').rstrip('\n')
                    prepared_doc = f'{prepared_doc}\n\nWhere: {one_mod_path}'
                    docs_map[inner_key] = prepared_doc
    for one_key in sorted(docs_map.keys()):
        print(f'{docs_map[one_key]}\n{"="*30}')
else:
    parser_inst.print_help()
