"""
The module provides parameter validation functions common across Metron's components. The scope of validation is all
parameters, except validation of YAML config parameters.
"""

import os
from typing import Any, Union
import typeguard


def check_type(variable: Any, expected_type: Any) -> None:
    """
    Validates if given <variable> is type of <expected_type>.

    Args:
        variable (Any): Variable.
        expected_type (Any): Type.

    Returns (None):

    Exceptions:
        TypeError: Raised if <variable> is not type of <expected_type>.

    """
    typeguard.check_type("variable", variable, expected_type)


def check_file_existence(file_path: str) -> None:
    """
    Validates if file path exists and is a file.

    Args:
        file_path (str): File path.

    Returns (None):

    Exceptions:
        OSError: If file does not exist or path is not a file.
    """
    type_check(file_path, str)
    if not os.path.exists(file_path):
        raise OSError(f"Path `{file_path}` does not exist.")
    if not os.path.isfile(file_path):
        raise OSError(f"Path `{file_path}` exists but it is not a file.")


def check_folder_existence(folder_path: str) -> None:
    """
    Validates if file path exists and is a folder.

    Args:
        folder_path (str): Folder path.

    Returns (None):

    Exceptions:
        OSError: If file does not exist or path is not a folder.
    """
    type_check(folder_path, str)
    if not os.path.exists(folder_path):
        raise OSError(f"Path `{folder_path}` does not exist.")
    if os.path.isfile(folder_path):
        raise OSError(f"Path `{folder_path}` exists but it is not a folder.")


def check_parameter_value_in_range(
    param_value: Union[int, float], lower_bound: Union[int, float], upper_bound: Union[int, float]
) -> None:
    """
    Checks if parameter value is in range <<lower_bound>, <upper_bound>>.

    Args:
        param_value (Union[int, float]): Parameter value.
        lower_bound (Union[int, float]): Lower bound of allowed parameter values.
        upper_bound (Union[int, float]): Upper bound of allowed parameter values.

    Returns (None):

    Exceptions:
        ValueError: If value is not in the range.
    """
    type_check(param_value, (int, float))
    type_check(lower_bound, (int, float))
    type_check(upper_bound, (int, float))
    if param_value < lower_bound or param_value > upper_bound:
        raise ValueError(f"Given `{param_value}` is out of the allowed range" f" <{lower_bound}, {upper_bound}>.")
