"""
Utils module for I/O.
"""

import os
import logging
from shutil import rmtree
from os import path
from . import param_validators as param_val

def force_folder_create(fs_folder_path: str) -> None:
    param_val.check_type(fs_folder_path, str)

    head, _ = path.split(fs_folder_path)
    param_val.check_folder_existence(head)
    if path.isdir(fs_folder_path):
        rmtree(fs_folder_path)
        logging.warn("Forced creation of `%s` folder.", fs_folder_path)
        os.mkdir(fs_folder_path)