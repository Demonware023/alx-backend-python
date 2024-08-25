#!/usr/bin/env python3
"""
test_public_repos_url
"""
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for the GithubOrgClient class.
    """

    @patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test that _public_repos_url returns the expected URL based on the mocked org property.

        Args:
            mock_org (PropertyMock): The mock object for the org property.
        """
        # Define the mock payload to be returned by the org property
        mock_org.return_value = {
            'repos_url': 'https://api.github.com/orgs/test-org/repos'
        }

        # Create an instance of GithubOrgClient
        client = GithubOrgClient('test-org')

        # Expected URL based on the mock payload
        expected_url = 'https://api.github.com/orgs/test-org/repos'

        # Check that _public_repos_url returns the expected URL
        self.assertEqual(client._public_repos_url, expected_url)
