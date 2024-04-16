#!/usr/bin/env python3
# part of python-functions Copyright (C) 2024 Tamas Viktor Krizsan
# <https://github.com/tamasviktorkrizsan>
# License: GPL-3.0-or-later
"""This module contains python related settings."""

import sys

import os

import json

import design_patterns


# TODO: modify this class, to extract settings from a env file

class UserSettings(metaclass=design_patterns.SingletonMeta):
    """This class storing environment settings for python-functions.

        Attributes:

            _ABSOLUTE_PATH(bool): allow or disallow the creation of absolute paths (true/false).

            _PRODUCTION_BYTE_CODE_WRITE(bool): allow or disallow the creation of pycache files, when not run through
            the unittest module (true/false).

    """
    def __init__(self, user_settings_file='python_user_settings.json'):

        json_file = open(os.path.join(os.path.dirname(__file__), user_settings_file))

        user_setting = json.load(json_file)

        self._ABSOLUTE_PATH = user_setting['ABSOLUTE_PATH']

        self._PRODUCTION_BYTE_CODE_WRITE = user_setting['PRODUCTION_BYTE_CODE_WRITE']

        json_file.close()

        if 'unittest' not in sys.modules and self._PRODUCTION_BYTE_CODE_WRITE == 'false':

            sys.dont_write_bytecode = True

    @property
    def absolute_path(self) -> bool:
        return self._ABSOLUTE_PATH
