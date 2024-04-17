#!/usr/bin/env python3
# part of python-ffmpeg Copyright (C) 2024 Tamas Viktor Krizsan
# <https://github.com/tamasviktorkrizsan>
# License: GPL-3.0-or-later

"""This module contains file pattern processing functions."""


import os

import glob

import copy

import re

import _python_functions


def _pattern_list_2_object_list(input_object: object) -> list[object]:
    """generate an object list from a pattern list.

        this function will break down the parameter object's 'input_file' attribute, into several objects, depending
        on how many match the pattern globbing will find. This function is subservient to the make_object_list function.

            Args:

                input_object:
                    A object containing a pattern list in the input_file attribute. For example: ['*.ext1', '*.ext2'].

            Returns:
                A list of objects.
    """
    _env = _python_functions.UserSettings()

    _obj_list = []

    for i in input_object.input_file:

        for k in (glob.glob(i)):

            _job_item = copy.deepcopy(input_object)

            if _env.absolute_path is True:

                _job_item.input_file = os.path.abspath(k)

            else:

                _job_item.input_file = k

            _obj_list.append(_job_item)

    return _obj_list


def _pattern_2_object_list(input_object: object) -> list[object]:
    """generate an object list from a single pattern.

        this function will break it down the parameter object's 'input_file' attribute, into several objects,
        depending on how many match the pattern globbing will find. This function is subservient to the
        make_object_list function.

            Args:

                input_object:
                    A object containing a pattern in the input_file attribute. For example: '*.ext1'.

                Returns:
                    A list of objects.
    """

    _env = _python_functions.UserSettings()

    _obj_list = []

    for i in (glob.glob(input_object.input_file)):

        _job_item = copy.deepcopy(input_object)

        if _env.absolute_path is True:

            _job_item.input_file = os.path.abspath(i)

        else:

            _job_item.input_file = i

        _obj_list.append(_job_item)

    return _obj_list


def _exact_file_2_object_list(input_object: object) -> list[object]:
    """Put an object into a list.

          Object with exact filename in its 'object.input_file' attribute, will be put in a list for further processing.
          This function is subservient to the make_object_list function.

          Args:
            input_object: A object containing an exact filename in the input_file attribute.

          Returns:
            A object within a list
    """
    _obj_list = [input_object]

    return _obj_list


def make_object_list(input_object: object) -> list[object]:
    """Generate a list of objects based on the value of the object.input_file attribute.

        take the value of the 'object.input_file' attribute and generate a list of objects from it.
        this possible values of the input_file attribute are:

            pattern list: ['*.extension1','*.extension2']

            pattern: '*.extension'

            exact file: 'example.extension'

        Args:
            input_object: A object containing the input_file attribute.

        Returns:
            A list of objects with exact filenames in each object.input_file attribute.
    """

    if type(input_object.input_file) is list:

        obj_list = _pattern_list_2_object_list(input_object)

    elif re.match(r"\*", input_object.input_file):

        obj_list = _pattern_2_object_list(input_object)

    else:

        obj_list = _exact_file_2_object_list(input_object)

    return obj_list
