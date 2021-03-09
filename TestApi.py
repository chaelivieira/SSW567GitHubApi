# -*- coding: utf-8 -*-

import unittest

from api import repoApi

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestApi(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testValidID(self): 
        self.assertEqual(repoApi("chaelivieira"), )
    def testInvalidID(self): 
        self.assertEqual(repoApi("chaelvieira"), )
    def testValidRepo(self):
        self.assertEqual(repoApi("chaelivieira", "546Project"), )
    def testInvalidRepo(self):
        self.assertEqual(repoApi("chaelivieira", "invalidRepo"), )

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

