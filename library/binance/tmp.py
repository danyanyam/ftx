from enum import Enum


class Possible_Value(Enum):
    ONE_MINUTE = '1m'
    ONE_SECOND = '1sec'


def some_funny_finction(arg):

    assert arg in [n.value for n in Possible_Value], f'{arg} is not OK!'
    print(f'{arg} is OK!')


some_funny_finction('1m')
some_funny_finction(Possible_Value.ONE_MINUTE)


def some_nice_function(arg):

    if not isinstance(arg, Possible_Value):
        raise TypeError(f'{arg} is not OK!')

    print(f'{arg.value} is OK!')


some_nice_function(Possible_Value.ONE_MINUTE)
some_nice_function('1m')
