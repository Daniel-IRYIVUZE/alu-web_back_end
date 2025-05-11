#!/usr/bin/env python3
"""Given the parameters and the return values, add type annotations to the function."""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(
        dct: Mapping[Any, Any],
        key: Any,
        default: Union[T, None] = None
) -> Union[Any, T]:
    """Returns the value for a key in a dictionary, or a default value if the key is not found."""
    if key in dct:
        return dct[key]
    else:
        return default
