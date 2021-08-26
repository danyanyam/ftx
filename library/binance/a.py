from typing import Union


def config(a: int, b: int, c: int):
    return min(a, b, c)


def detele(a: bool, b: int, c: bool, d: Union[str, float, bool]):
    print(a * b)


detele(a=False, b=1, c=False, d=True)
