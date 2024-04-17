#!/usr/bin/env python3

import unittest

import object

from unittest.mock import Mock


class TestMakeObjectList(unittest.TestCase):

    def test_pattern_list_2_object_list(self):

        mock = Mock(input_file=['*.txt', '*.log'])

        object_list = object.make_object_list(mock)

        self.assertEqual(object_list[0].input_file, 'input_test_file_1.txt', '*.txt 1 doesnt work')

        self.assertEqual(object_list[1].input_file, 'input_test_file_2.txt', '*.txt 2 doesnt work')

        self.assertEqual(object_list[2].input_file, 'input_test_file_3.log', '*.log 3 doesnt work')

        self.assertEqual(object_list[3].input_file, 'input_test_file_4.log', '*.log 4 doesnt work')

    def test_pattern_2_object_list(self):

        mock = Mock(input_file='*.txt')

        object_list = object.make_object_list(mock)

        self.assertEqual(object_list[0].input_file, 'input_test_file_1.txt', '*.txt 1 doesnt work')

        self.assertEqual(object_list[1].input_file, 'input_test_file_2.txt', '*.txt 2 doesnt work')

    def test_exact_file_2_object_list(self):

        mock = Mock(input_file='input_test_file_1.txt')

        object_list = object.make_object_list(mock)

        self.assertEqual(object_list[0].input_file, 'input_test_file_1.txt', '*.txt 1 doesnt work')


if __name__ == '__main__':
    unittest.main()
