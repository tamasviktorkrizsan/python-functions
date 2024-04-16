#!/usr/bin/env python3

import unittest

import sys

import _python_functions


class TestPythonFunctions(unittest.TestCase):

    def setUp(self):
        self.settings = _python_functions.UserSettings()

    def tearDown(self):

        del self.settings

    def test_absolute_path(self):
        self.assertEqual(self.settings.absolute_path, "false", 'absolute_path getter is not working')

    def test_bytecode_writing_boolean(self):
        self.assertEqual(sys.dont_write_bytecode, False, 'bytecode writing is not working')


if __name__ == '__main__':
    unittest.main()
