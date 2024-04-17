#!/usr/bin/env python

import unittest

import file

import os


class TestMakeFolderName(unittest.TestCase):

    def test_make_folder_name(self):

        # Arrange & Act

        result = file.make_folder_name('OUTPUT')

        # Assert

        self.assertEqual(result, os.environ['USERPROFILE'] + r'\GitHub\python-functions\tests\OUTPUT',
                         'make_folder_name function is not working')


class TestMakeFilename(unittest.TestCase):

    def test_make_filename(self):

        # Arrange

        input_filename = 'D:\\files\\test file 1.mkv'

        output_format = '.264'

        # Act

        result = file.make_filename(input_filename, output_format)

        # Assert

        self.assertEqual(result, 'test_file_1.264', 'make_file_name function is not working')

    def test_make_filename_with_folder(self):

        # Arrange

        input_filename = 'D:\\files\\test file 1.mkv'

        output_format = '.264'

        # Act

        result = file.make_filename(input_filename, output_format, 'OUTPUT')

        # Assert

        self.assertEqual(result, 'OUTPUT\\test_file_1.264', 'make_file_name function is not working')


class TestScanExtension(unittest.TestCase):

    def setUp(self):

        # Arrange

        self.input_filename = 'test file 1.mkv'

    def test_scan_extension(self):

        # Act

        result = file.scan_extension(self.input_filename)

        # Assert

        self.assertEqual(result, '.mkv', 'scan_extension function is not working')


class TestSearchList(unittest.TestCase):

    def test_search_list(self):

        # Arrange

        input_filename = ["*.webm", "*.mp4", "*.mkv"]

        keyword = ".mkv"

        # Act

        result = file.search_list(input_filename, keyword)

        # Assert

        self.assertEqual(result, True, 'test_search_list function is not working')


class TestRenameWhitespace(unittest.TestCase):

    def test_rename_whitespace(self):

        # Arrange

        input_text = 'input_test_file_1.txt'

        # Act

        result = file.scan_extension(input_text)

        # Assert

        expected = '.txt'

        self.assertEqual(result, expected, 'scan_extension function is not working')


if __name__ == '__main__':
    unittest.main()
