#!/bin/bash
# part of python-ffmpeg Copyright (C) 2024 Tamas Viktor Krizsan
# <https://github.com/tamasviktorkrizsan>
# License: GPL-3.0-or-later

python -m coverage run -m unittest discover && python -m coverage report --omit=test_*;

# shellcheck disable=SC2162
read -p "Press enter to continue...";

