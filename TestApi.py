# -*- coding: utf-8 -*-

import unittest

from api import repoApi
from api import checkRepo
# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestApi(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testValidID(self): 
        self.assertEqual(repoApi("chaelivieira"),['Repo:546Project : Number of Commits: 1', 'Repo:cs146-example : Number of Commits: 8', 'Repo cs392--perm_sec_b is empty', 'Repo:help : Number of Commits: 3', 'Repo:joanielovesHP : Number of Commits: 1', 'Repo lab3 is empty', 'Repo:MARCK : Number of Commits: 30', 'Repo:SSW567 : Number of Commits: 4', 'Repo:SSW567GitHubApi : Number of Commits: 5', 'Repo:SSW567HW2a : Number of Commits: 11'] )
    def testInvalidID(self): 
        self.assertEqual(repoApi("chaelvieira"),{'message': 'Not Found', 'documentation_url': 'https://docs.github.com/rest/reference/repos#list-repositories-for-a-user'} )
    def testValidRepo(self):
        self.assertEqual(checkRepo("chaelivieira", "MARCK"), 30)
    def testInvalidRepo(self):
        self.assertEqual(checkRepo("chaelivieira","invalidRepo"), {'message': 'Not Found', 'documentation_url': 'https://docs.github.com/rest/reference/repos#list-commits'})
    def testEmptyRepo(self):
        self.assertEqual(checkRepo("chaelivieira", "lab3"),{'message': 'Git Repository is empty.', 'documentation_url': 'https://docs.github.com/rest/reference/repos#list-commits'})

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

