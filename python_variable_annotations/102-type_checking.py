#!/usr/bin/env python3
"""
This script defines a function that zooms into an array by repeating its elements.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """Return a new list where each element of the tuple is repeated 'factor' times."""
    zoomed_in: List[int] = [item for item in lst for _ in range(factor)]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
