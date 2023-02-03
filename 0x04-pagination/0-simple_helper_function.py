#!/usr/bin/env python3
def index_range(page, page_size):
    # Calculate the start index by multiplying (page - 1) by page_size
    start_index = (page - 1) * page_size

    # Calculate the end index by adding the start index to the page_size
    end_index = start_index + page_size

    # Return the start and end indices as a tuple
    return (start_index, end_index)
