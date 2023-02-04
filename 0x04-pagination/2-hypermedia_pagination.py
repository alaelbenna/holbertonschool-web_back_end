#!/usr/bin/env python3
"""Simple pagination module"""

import csv
import math
from typing import Dict, List, Tuple

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""

        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return the appropriate page of the dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        self.dataset()
        correct_index = index_range(page, page_size)
        if correct_index[0] > len(self.__dataset):
            return []
        return self.__dataset[correct_index[0]:correct_index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        get_hyper: returns a dictionary containing nemours key value data
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        next_page, prev_page = None, None

        if page < total_pages:
            next_page = page + 1
        if page > 1:
            prev_page = page - 1

        return {'page_size': page_size, 'page': page, 'data': data,
                'next_page': next_page, 'prev_page': prev_page,
                'total_pages': total_pages}
