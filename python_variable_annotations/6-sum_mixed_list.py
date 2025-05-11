#!/usr/bin/env python3
"""Complex types - mixed list."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Type-annotated function that returns the sum of a list of integers and floats."""
    return sum(mxd_lst)
