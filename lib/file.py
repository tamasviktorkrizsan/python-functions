#!/usr/bin/env python3
# part of python-ffmpeg Copyright (C) 2024 Tamas Viktor Krizsan
# <https://github.com/tamasviktorkrizsan>
# License: GPL-3.0-or-later

""" This module contains file or folder related general operations, including naming, search."""


import pathlib

import re


def convert_raw_string(input_string: str):
    """Convert a normal string to a raw string. Useful for handling dos style paths.

        Arguments:

            input_string(str): A normal string.

        Returns:

            A raw string.
    """

    raw_folder_path = r"{}".format(input_string)

    return raw_folder_path


def search_list(input_list: list, input_pattern: str) -> bool:
    """Search in list for pattern.

        Find out if the given pattern has at least 1 match among the input list's items.

        Args:

            input_list(list[str]): A list of strings. For example: ["*.mp4", "*.mkv"].

            input_pattern(str): A string type pattern. For example: ".mkv"

        Returns:
            Boolean (True/False)
    """

    pattern = convert_raw_string(input_pattern)

    for list_item in input_list:
        if re.search(pattern, list_item, re.IGNORECASE):
            return True
    return False


def filter_filename(input_filename: str) -> str:
    """Filter file or folder names with filesystem problematic characters.

        Replace filesystem problematic characters in filenames, to make it more OS/Shell/aesthetic friendly.
        Ordinary filenames will be returned untouched.
        The following characters will be replaced:

        Original character -> new character
        Whitespace(" ") -> Underscore("_")

        Args:
            input_filename(str): filename string.

        Returns:
            Corrected or untouched filename string.
    """

    # TODO: expand this function with more replace patterns

    return input_filename.replace(" ", "_")


def make_folder_name(output_folder_name: str):
    """Create an output folder name with path for output shell commands.

        Args:
            output_folder_name(str): folder name string.

        Returns:
            folder path in a raw string (for dos style paths).
    """

    folder_path = str(pathlib.Path.cwd().joinpath(output_folder_name))

    raw_folder_path = convert_raw_string(folder_path)

    return raw_folder_path


def make_filename(input_filename: str, suffix: str = '', input_folder_name: str = None):
    """Create an output filename for output shell commands.

        Args:

            input_filename(str): filename string.

            suffix(str): added ending to the filename with the file extension included.

            input_folder_name(str): optional. It will concat the filename with a folder or absolute path.

        Returns:
            filename or full path in a raw string (for windows style paths).
    """

    filename = pathlib.Path(input_filename)

    output_filename = filter_filename(filename.stem) + suffix

    if input_folder_name is None:

        return convert_raw_string(str(output_filename))

    else:

        folder_name = pathlib.Path(input_folder_name)

        output_path = convert_raw_string(str(folder_name.joinpath(output_filename)))

        return output_path


def scan_extension(input_filename: str) -> str:
    """Get the input file name's extension.

        Extract the input file's extension.

        Args:
            input_filename(str): string.

        Returns:
            file extension in the following format: ".extension"
    """

    filename = pathlib.Path(input_filename)

    extension = filename.suffix

    return extension
