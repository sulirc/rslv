from enum import IntEnum


RSLV_TITLE = "[bold]\[rslv] ~>[/bold]"


class ExitStatus(IntEnum):
    """Program exit status code constants."""
    SUCCESS = 0
    ERROR = 1
    ERROR_TIMEOUT = 2

    # 128+2 SIGINT
    # <http://www.tldp.org/LDP/abs/html/exitcodes.html>
    ERROR_CTRL_C = 130
