#!/usr/bin/env python3
'''Copy index_range from the previous task and the
following class into your code'''
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''Func should return a tuple of size two containing
    a start index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination parameters.'''
    end = page * page_size
    start = end - page_size
    return (start, end)


class Server:
    """class server to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """class Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Func that Use assert to verify that both arguments are integers greater
        than 0, Use index_range to find the correct indexes to paginate
        the dataset correctly and return the appropriate page of the
        dataset (i.e. the correct list of rows).'''
        assert isinstance(page_size, int) and isinstance(page, int)
        assert (page > 0 and page_size > 0)
        self.dataset()
        res = index_range(page, page_size)
        return self.__dataset[res[0]:res[1]]