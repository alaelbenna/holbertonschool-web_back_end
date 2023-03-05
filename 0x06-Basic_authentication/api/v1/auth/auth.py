#!/usr/bin/env python3
"""auth module"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class"""

    def __init__(self):
        """Constructor"""
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """return path, excluded_path, otherwise False"""
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        for p in excluded_paths:
            if p == path:
                return False
            if p.endswith('*'):
                suffixed_path = p[:-1]
                if suffixed_path in path:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """return request, otherwise None"""
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """return request, otherwise None"""
        return None