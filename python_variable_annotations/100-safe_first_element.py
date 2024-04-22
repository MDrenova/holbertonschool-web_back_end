#!/usr/bin/env python3
"""Complex types - functions"""


from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """duck-typed annotations"""
    if lst:
        return lst[0]
    else:
        return None
