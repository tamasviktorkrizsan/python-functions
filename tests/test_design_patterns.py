#!/usr/bin/env python3

import unittest

import design_patterns


class TestSingletonMeta(unittest.TestCase):

    def test_SingletonMeta(self):
        s1 = design_patterns.SingletonMeta
        s2 = design_patterns.SingletonMeta

        self.assertEqual(id(s1), id(s2), "Singleton class unit test failed, variables containing different instances.")


if __name__ == '__main__':
    unittest.main()
