#!/usr/bin/env python3
"""test_utils test module"""

from parameterized import parameterized
import requests
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""

    @parameterized.expand([
        ({'a': 1}, ('a'), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test that the method returns what it is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a')),
        ({'a': 1}, ('a', 'b'))
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test that a KeyError is raised for a given inputs"""
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """TestGetJson class"""

    @parameterized.expand([
        ({"test_url": "http://example.com"}, {"test_payload": True}),
        ({"test_url": "http://holberton.io"}, {"test_payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """"""
        with patch('requests.get') as mock_request:
            mock_request.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mock_request.assert_called_once()


class TestMemoize(unittest.TestCase):
    """TestMemoize class"""

    def test_memoize(self):
        """test memoization function return the same value"""
        class TestClass:
            """TestClass class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                """return a_method result"""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_test:
            mock_test.return_value = 42
            test = TestClass()
            self.assertEqual(test.a_property, mock_test.return_value)
            mock_test.assert_called_once()


if __name__ == '__main__':
    unittest.main()