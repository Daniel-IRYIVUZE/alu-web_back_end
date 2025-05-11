#!/usr/bin/env python3
"""Given the parameters and the return values, add type annotations to the function."""

from typing import Mapping, Any, Union, Optional, TypeVar

T = TypeVar('T')

def safely_get_value(
        dct: Mapping[Any, Any],
        key: Any,
        default: Optional[T] = None
) -> Union[Any, T]:
    """Return the value for a key in a dictionary, or a default value if the key is not found."""
    if key in dct:
        return dct[key]
    return default
