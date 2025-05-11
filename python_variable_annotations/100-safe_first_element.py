#!/usr/bin/env python3
"""Augment the following code with the correct duck-typed annotations."""

from typing import Sequence, Any

def safe_first_element(lst: Sequence[Any]) -> Any:
    """Return the first element of a sequence, or None if the sequence is empty."""
    if lst:
        return lst[0]
    return None
