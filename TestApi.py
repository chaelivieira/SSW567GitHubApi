# -*- coding: utf-8 -*-

import unittest
import json
from api import repoApi
from api import checkRepo
from api import getCommits
from unittest.mock import Mock, patch


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestApi(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    @patch('api.requests.get')
    def test_repoApi(self, mock_get):
     
        with open('./mockJsons/repos.json') as f:
            data = json.load(f)
        a = data
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = a
        response = repoApi("chaelivieira")
        #print(response)
        self.assertEqual(response,['546Project', 'cs146-example', 'cs392--perm_sec_b', 'help', 'joanielovesHP', 'lab3', 'MARCK', 'SSW567', 'SSW567GitHubApi', 'SSW567HW2a'])
    
    @patch('api.requests.get')
    def test_commits(self, mock_get):
        with open('./mockJsons/hw2a.json') as f:
            data = json.load(f)
        k = data
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = k
        response = getCommits("chaelivieira", "SSW567HW2a")
        self.assertEqual(response,"Repo:SSW567HW2a : Number of Commits: 12")

    @patch('api.requests.get')
    def test_invalid_repo(self, mock_get):
        with open('./mockJsons/errorRepo.json') as f:
            data = json.load(f)
        k = data
        mock_get.return_value.json.return_value = k
        response = repoApi("chaelivieira")
        self.assertEqual(response,{'message': 'Not Found', 'documentation_url': 'https://docs.github.com/rest/reference/repos#list-repositories-for-a-user'} )
       
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

