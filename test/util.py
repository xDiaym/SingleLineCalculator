import os
import subprocess


PATH = os.path.join(os.getcwd(), 'slrpn.py')


def call(expression: str) -> float:
    args = expression.split()
    raw_out = subprocess.check_output(('python', PATH, *args))
    return float(raw_out.decode('utf8'))
