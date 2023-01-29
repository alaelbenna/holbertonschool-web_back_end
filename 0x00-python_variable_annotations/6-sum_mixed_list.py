#!/usr/bin/env python3
'''
func Complex types - mixed list
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    type-annotated func sum_mixed_list which takes
    a list mxd_lst of floats and integers and returns
    their sum as a float.
    '''
    return sum(mxd_lst)