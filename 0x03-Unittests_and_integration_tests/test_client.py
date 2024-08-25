#!/usr/bin/env python3
"""
TestIntegrationGithubOrgClient
"""
import unittest
from unittest.mock import patch
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test case for the GithubOrgClient class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test class by patching requests.get to return mock data.
        """
        # Patch requests.get and set up side effects based on URL
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Define side effects for different URLs
        def side_effect(url):
            if url == 'https://api.github.com/orgs/test-org':
                return MockResponse(org_payload)
            elif url == 'https://api.github.com/orgs/test-org/repos':
                return MockResponse(repos_payload)
            raise ValueError('Unexpected URL')

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the test class by stopping the patcher.
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test that public_repos returns the expected repositories.
        """
        # Create an instance of GithubOrgClient
        client = GithubOrgClient('test-org')

        # Call the public_repos method
        repos = client.public_repos()

        # Verify that the public_repos returns the expected list of repositories
        self.assertEqual(repos, expected_repos)

class MockResponse:
    """
    Mock class for requests' Response object.
    """
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data
