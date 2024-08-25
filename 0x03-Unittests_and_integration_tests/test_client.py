#!/usr/bin/env python3
"""
TestGithubOrgClient
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for the GithubOrgClient class.
    """

    @patch('client.get_json')
    @parameterized.expand([
        ('google', {'login': 'google'}),
        ('abc', {'login': 'abc'}),
    ])
    def test_org(self, org_name, mock_payload, mock_get_json):
        """
        Test that GithubOrgClient.org returns the expected result based on the mocked get_json.

        Args:
            org_name (str): The organization name to be tested.
            mock_payload (dict): The payload returned by the mocked get_json call.
            mock_get_json (Mock): The mock object for the get_json function.
        """
        # Set up the mock to return the expected payload
        mock_get_json.return_value = mock_payload

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Ensure get_json was called with the expected URL
        expected_url = f'https://api.github.com/orgs/{org_name}'
        mock_get_json.assert_called_once_with(expected_url)

        # Check that the org property returns the expected result
        self.assertEqual(client.org, mock_payload)
