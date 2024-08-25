#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map function with various inputs.

        Args:
            nested_map (dict): The nested dictionary to be tested.
            path (tuple): The path to access the value.
            expected (any): The expected result of the access.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "Key not found: 'a'"),
        ({"a": 1}, ("a", "b"), "Key not found: 'b'"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_message):
        """
        Test access_nested_map function raises KeyError with expected message.

        Args:
            nested_map (dict): The nested dictionary to be tested.
            path (tuple): The path to access the value.
            expected_message (str): The expected error message.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), expected_message)
