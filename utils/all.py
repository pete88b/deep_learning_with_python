import importlib
from pathlib import Path
for py_file in Path('utils').glob('*.py'):
    if 'all' == py_file.stem:
        continue # we'll import every .py file in utils except utils/all.py
    module = importlib.import_module(f'utils.{py_file.stem}')
    # make everything in __all__ available via the current scopes global variables
    globals().update({k: getattr(module, k) for k in module.__all__})
    # this is like doing a `from module import *`
