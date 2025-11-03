"""Metron Shared utilities."""

import sys

def is_debug_enabled() -> bool:
    """Checks if any of following conditions is met:
        a) Python script is not called with `-O` optimize flag
        b) Debugger is attached

    Returns:
        bool: _description_
    """
    
    if __debug__ or sys.gettrace():
        return True
    else:
        return False