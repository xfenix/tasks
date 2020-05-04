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
    for one_mod_path in current_dir.glob('part_*.py'):
        if one_mod_path.is_file():
            one_module: types.ModuleType = importlib.import_module(f'.{one_mod_path.stem}', package='tasks')
            classes_list: typing.List = inspect.getmembers(one_module, inspect.isclass)
            for class_title, one_class_obj in classes_list:
                if class_title.endswith('Task'):
                    first_line: int = inspect.getsourcelines(one_class_obj)[1]
                    inner_key: str = inspect.getdoc(one_class_obj).split('\n')[0].rstrip('.').lstrip('Task #')
                    docs_map[inner_key] =\
                        f"{inspect.getdoc(one_class_obj).replace(' ' * 4, '')}\n\nWhere: {one_mod_path}:{first_line}"
    for one_key in sorted(docs_map.keys()):
        print(f'{docs_map[one_key]}\n{"="*30}')
else:
    parser_inst.print_help()
