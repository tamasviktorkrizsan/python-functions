# python-functions

![version 3.10](https://img.shields.io/badge/Python-3.10-blue) ![96% coverage](https://img.shields.io/badge/coverage-96%25-green) ![codes tyle](https://img.shields.io/badge/code%C2%A0style-Google-blue)

Basic library tools/dependency for other python based projects.


## Dependencies

- python 3.10 <=


## Installation

Set the PATH environmental variable to the directory where you want store your library
files and copy the contents of the "lib" folder into.


## Usage

At the top of your client code, following the shebang `#!/usr/bin/env python3` line
include one of the modules.

After that, you can call these functions/classes/methods...


## Library Modules

### design patterns module

#### Singleton meta (class)

Limit the number of created objects to 1.
The client class has to inherit it as a metaclass.

**Example**

`class ClientClass(metaclass=design_patterns.SingletonMeta):`

***

### file module

#### convert_raw_string (function)

Convert a normal string to a raw string.
            
**Arguments:** 

input_string(str): A normal string.

**Returns:**

A raw string.

***

#### search_list (function)

Search in a list for pattern.

Find out if a given pattern has 1 match in one of the input list's items.

**Arguments**:

**input_list(list[str]):** A list of strings. For example: `["*.mp4", "*.mkv"]`.

**input_pattern(str):** A string type pattern. For example: `".mkv"`

**Returns:**

Boolean (True/False)

***

#### filter_filename (function)

Filter file or folder names with filesystem problematic characters.

Replace filesystem problematic characters in filenames, to make it more OS/Shell/aesthetic friendly. 
Ordinary filenames will be returned untouched.

The following characters will be replaced:

**Original character -> new character**

Whitespace(" ") -> Underscore("_")

**Arguments:**

**input_filename(str):** filename string.

**Returns:**

Corrected or untouched filename string.
                
***

#### make_folder (function)

Recursively create multiple folders.

**Arguments:**

**folder_list(list[str]):** a list consist of folder name strings.

**Raises:**

FileExistsError: An error occurred when the given folder is already exists.

***

#### make_folder_name (function)

Create an output folder name with path for output shell commands.


**Arguments:**

**output_folder_name(str):** folder name string.


**Returns:**

folder path in a raw string (for dos style paths).
    
***

#### make_filename (function)

Create an output filename for output shell commands.

**Arguments:**

**input_filename(str):** filename string.

**suffix(str):** added ending to the filename with the file extension included.

**input_folder_name(str):** optional. It will concat the filename with a folder or absolute path.

**Returns:**

filename or full path in a raw string (for windows style paths).

***

#### scan_extension (function)

Get the input file name's extension.

Extract the input file's extension.

**Arguments:**

**input_filename(str):** string.

**Returns:**

file extension in the following format: ".extension"

***

### object module

#### make_object_list (function)

Generate a list of objects based on the value of the object.input_file attribute.

take the value of the 'object.input_file' attribute and generate a list of objects from it.
this possible values of the input_file attribute are:

- pattern list: `['*.extension1','*.extension2']`

- pattern: `'*.extension'`

- exact file: `'example.extension'`

**Arguments:**

**input_object:** A object containing the input_file attribute.

**Returns:**

A list of objects with exact filenames in each object.input_file attribute.

***

### process module

#### start (function)

Execute a shell command.

Loop through a list of dictionaries and execute the 'command' key in each dict, furthermore this function can
create output folders, and record the contents of the shell into a logfile if the necessary values for the
'output_folder_list' and/or 'logfile' keys are present.

**Arguments:**

**command_object_list(list[dict]):** 

a list of dictionaries. The dictionaries must contain the following keys...

**command(list[str]):**

A list containing a valid shell command, broken down to tokens.
Example: `'[program, -programSwitch1, -programSwitch2, outputFile]'`

**output_folder_list(list[str]):** 

Optional key. A list containing output folder names, that are needed to be created.

**logfile(str):** 

Optional key. An output logfile name, all contents of the console goes here.

**Returns:**

Only returns the command, when the 'unittest' module is among the loaded modules.
        
***

#### return value (function)

Execute a shell command and return its output.

**Arguments:**

command(list[str]): A list containing a valid shell command, broken down to tokens. 
Example: '[program, -programSwitch1, -programSwitch2, outputFile]'

**Returns:**

string.


## Developer notes

### code style

The code in this repository formatted according the standards of the Google Style Guides.
If you want to contribute to this project, then read the guide first.

https://google.github.io/styleguide/pyguide.html

for commits:

https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#type


## Sources

https://en.wikipedia.org/wiki/Filename#Reserved_characters_and_words
