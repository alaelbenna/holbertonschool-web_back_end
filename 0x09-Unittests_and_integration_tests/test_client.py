#!/usr/bin/env python3
""" test client module """

from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class to test client.GithubOrgClient"""

    @parameterized.expand([
        ("google", {}),
        ("abc", {})
        ])
    @patch("client.get_json")
    def test_org(self, url, result, mock):
        """test that GithubOrgClient.org returns the correct value"""
        mock.return_value = {}
        a = GithubOrgClient(url)
        self.assertEqual(a.org, result)
        mock.assert_called_once()

    def test_public_repos_url(self):
        """Test that the result of _public_repos_url is the expected
        one based on the mocked payload
        """
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as m:
            m.return_value = {"repos_url": "http://m.url"}
            t = GithubOrgClient("xyz")
            a = t._public_repos_url
            self.assertEqual(a, m.return_value.get("repos_url"))

    @patch("client.get_json")
    def test_public_repos(self, mock_test):
        """test that the list of repos is what you expect
        from the chosen payload
        """
        mock_test.return_value = [
            {"user_name": "repo_num_1"},
            {"user_name": "repo_num_2"}
        ]
        mock_test()
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as p_repos:
            p_repos.return_value = [
                {"user_name": "repo_num_1"},
                {"user_name": "repo_num_2"}
            ]
            a = GithubOrgClient('xyz')
            t = a._public_repos_url
            self.assertEqual(t, p_repos.return_value)
            p_repos.assert_called_once()
            mock_test.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """test GithubOrgClient.has_license"""
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key),
            expected_result
        )


if __name__ == '__main__':
    unittest.main()