#!/usr/bin/env python3
"""
implement the TestIntegrationGithubOrgClient class with the test_public_repos
and test_public_repos_with_license methods
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
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

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
        Test that public_repos returns the expected list of repositories.
        """
        client = GithubOrgClient('test-org')
        repos = client.public_repos()
        self.assertEqual(repos, expected_repos)

    def test_public_repos_with_license(self):
        """
        Test that public_repos with a license filter returns the expected list of repositories.
        """
        client = GithubOrgClient('test-org')
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, apache2_repos)

class MockResponse:
    """
    Mock class for requests' Response object.
    """
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data
