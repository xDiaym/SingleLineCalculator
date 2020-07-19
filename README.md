# Single Line RPN
[![CI](https://github.com/xDiaym/SingleLineCalculator/workflows/CI/badge.svg)](https://github.com/xDiaym/SingleLineCalculator/actions?query=workflow%3ACI)  
One of the shortest RPN calculator in 1 line; 245 characters

## Usage
```shell script
# For infix notation
$ python slinfix.py <expression>
# For postfix notation
$ python slpostfix.py <expression>
```
Example:
```shell script
$ python slinfix.py 2 + 2
4.0
```

## Testing
```shell script
$ python -m unittest
```

## License
[The MIT License](https://opensource.org/licenses/MIT)
