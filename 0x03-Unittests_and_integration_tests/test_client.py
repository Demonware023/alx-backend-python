#!/usr/bin/env python3
"""
Test_public_repos
"""
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for the GithubOrgClient class.
    """

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test that public_repos returns the expected list of repositories and ensures 
        that the mocked _public_repos_url and get_json are called as expected.
        """

        # Mock _public_repos_url to return a specific URL
        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            # Define the mock payload to be returned by get_json
            mock_payload = [
                {'name': 'repo1'},
                {'name': 'repo2'},
                {'name': 'repo3'}
            ]
            mock_get_json.return_value = mock_payload

            # Define the mock URL to be returned by _public_repos_url
            mock_public_repos_url.return_value = 'https://api.github.com/orgs/test-org/repos'

            # Create an instance of GithubOrgClient
            client = GithubOrgClient('test-org')

            # Expected list of repositories
            expected_repos = ['repo1', 'repo2', 'repo3']

            # Call the public_repos method
            repos = client.public_repos()

            # Verify that public_repos returns the expected list of repositories
            self.assertEqual(repos, expected_repos)

            # Verify that _public_repos_url was called once
            mock_public_repos_url.assert_called_once()

            # Verify that get_json was called once with the mocked URL
            mock_get_json.assert_called_once_with('https://api.github.com/orgs/test-org/repos')
