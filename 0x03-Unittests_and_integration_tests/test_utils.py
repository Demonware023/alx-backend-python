#!/usr/bin/env python3
"""
TestGetJson
"""
import unittest
from unittest.mock import patch, Mock
from utils import get_json


class TestGetJson(unittest.TestCase):
    """
    Test case for the get_json function.
    """

    @patch('requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test get_json function returns expected result without making actual HTTP calls.

        Args:
            test_url (str): The URL to be passed to get_json.
            test_payload (dict): The payload to be returned by the mocked requests.get call.
            mock_get (Mock): The mock object for requests.get.
        """
        # Create a Mock response object with a json method that returns the test_payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the get_json function
        result = get_json(test_url)

        # Verify that requests.get was called exactly once with test_url
        mock_get.assert_called_once_with(test_url)

        # Verify that the result of get_json is equal to the test_payload
        self.assertEqual(result, test_payload)
