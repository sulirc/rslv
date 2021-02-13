#!/usr/bin/env python3
"""The main entry point. Invoke as `rslv` or `python -m cli`

"""
import sys
from .const import ExitStatus


def main():
    try:
        from .core import main

        exit_status = main()
    except KeyboardInterrupt:
        exit_status = ExitStatus.ERROR_CTRL_C

    sys.exit(exit_status.value)


if __name__ == "__main__":
    main()
