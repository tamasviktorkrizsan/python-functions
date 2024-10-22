#!/usr/bin/env python3
# part of python-ffmpeg Copyright (C) 2024 Tamas Viktor Krizsan
# <https://github.com/tamasviktorkrizsan>
# License: GPL-3.0-or-later
"""This module contains (disc writing) shell operations, such as folder making and command execution"""

import subprocess

import os

import sys


def make_folder(folder_list: list[str]) -> any:
    """Recursively create multiple folders.

        Args:
            folder_list: a list consist of folder name strings.

        Raises:
            FileExistsError: An error occurred when the given folder is already exists.
    """

    for folder in folder_list:

        try:

            os.makedirs(folder, mode=0o777, exist_ok=False)

        except FileExistsError:

            print(folder + " is already exists")


def start(command_object_list: list[dict]) -> any:
    """Execute a shell command.

        Loop through a list of dictionaries and execute the 'command' key in each dict, furthermore this function can
        create output folders, and record the contents of the shell into a logfile if the necessary values for the
        'output_folder_list' and/or 'logfile' keys are present.


        Args:

            command_object_list(list[dict]): a list of dictionaries. The dictionaries must contain the following keys...

                command(list[str]):

                    A list containing a valid shell command, broken down to tokens.
                    Example: '[program, -programSwitch1, -programSwitch2, outputFile]'

                output_folder_list(list[str]):

                    Optional key. A list containing output folder names, that are needed to be created.

                logfile(str):

                    Optional key. An output logfile name, all contents of the console goes here.

                Returns:
                    Only returns the command, when the 'unittest' module is among the loaded modules.
        """

    if 'unittest' in sys.modules:

        for i in command_object_list:

            print('\n SIMULATED TEST RESULTS: \n')

            print('\n COMMAND: \n')

            print(i['command'])

            if 'output_folder_list' in i.keys():

                print(' \n OUTPUT FOLDER LIST: \n')

                print(i['output_folder_list'])

            if 'logfile' in i.keys():

                print('\n LOGFILE: \n')

                print(i['logfile'])

        return command_object_list

    else:

        for i in command_object_list:

            # create folder(s)

            if i['output_folder_list'] is not None:

                make_folder(i['output_folder_list'])

            # execute command with/without logging
            # ignore errors enabled for bypassing files with unicode characters

            if i['logfile'] is None:

                subprocess.Popen(i['command'], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT, bufsize=1, shell=True, universal_newlines=True,
                                 errors="ignore", close_fds=True)

            else:

                with subprocess.Popen(i['command'], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                      stderr=subprocess.STDOUT, bufsize=1, shell=True, universal_newlines=True,
                                      errors="ignore", close_fds=True) as p, open(i['logfile'], 'w') as process_item:

                    for line in p.stdout:
                        print(line, end='')
                        process_item.write(line)

                    process_item.close()


def return_value(command):
    """Execute a shell command and return its output.

            Args:

                    command(list[str]):

                        A list containing a valid shell command, broken down to tokens.
                        Example: '[program, -programSwitch1, -programSwitch2, outputFile]'

                    Returns:
                        string.
    """
    output = subprocess.check_output(command, shell=True)

    return output


def return_code(command):
    """Execute a shell command and return its return code.

            Args:

                    command(list[str]):

                        A list containing a valid shell command, broken down to tokens.
                        Example: '[program, -programSwitch1, -programSwitch2, outputFile]'

                    Returns:
                        int.
    """
    result = subprocess.run(command).returncode

    return result
