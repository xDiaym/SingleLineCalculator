import subprocess
import sys
from os import PathLike

PYTHON_INTERPRETER_PATH = sys.executable


def call(script: PathLike, expression: str) -> float:
    args = expression.split()
    raw_out = subprocess.check_output((PYTHON_INTERPRETER_PATH, script, *args))
    return float(raw_out.decode('utf8'))
