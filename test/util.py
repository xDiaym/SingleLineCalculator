import os
import subprocess
import sys

PYTHON_INTERPRETER_PATH = sys.executable
SCRIPT_PATH = os.path.join(os.getcwd(), 'slrpn.py')


def call(expression: str) -> float:
    args = expression.split()
    raw_out = subprocess.check_output((PYTHON_INTERPRETER_PATH, SCRIPT_PATH,
                                       *args))
    return float(raw_out.decode('utf8'))
