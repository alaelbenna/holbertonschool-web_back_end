#!/usr/bin/env python3
"""simple helper function"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    index_range: a function that takes 2 integers the start index
    and the end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters.

    Args:
        page (int): the start index
        page_size (int): the end index

    Return: a tuple
    """
    page = (page - 1) * page_size
    return (page, page + page_size)
