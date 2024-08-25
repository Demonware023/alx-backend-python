#!/usr/bin/env python3
"""
Test_has_license
"""
import unittest
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for the GithubOrgClient class.
    """

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test that has_license correctly identifies whether a given license key is present 
        in the repository's license information.

        Args:
            repo (dict): The repository information to be tested.
            license_key (str): The license key to search for.
            expected (bool): The expected result of the has_license method.
        """
        # Create an instance of GithubOrgClient
        client = GithubOrgClient('test-org')

        # Use a mock for the _public_repos_url to return a predefined list
        with patch.object(client, '_public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            # Mock the response of public_repos to return the test repo
            with patch.object(client, 'public_repos', return_value=[repo]) as mock_public_repos:
                # Call the has_license method
                result = client.has_license(license_key)

                # Verify that public_repos was called once
                mock_public_repos.assert_called_once()
                
                # Check if has_license returns the expected result
                self.assertEqual(result, expected)
